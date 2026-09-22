import serial
import time
import pytest

def read_arduino_output(port='COM3', baudrate=9600, timeout=10):
    """
    Read DHT11 output from Arduino Serial Monitor
    Returns: list of readings
    """
    ser = serial.Serial(port, baudrate, timeout=timeout)
    time.sleep(2)  # Wait for Arduino to initialize
    
    readings = []
    start_time = time.time()
    
    while time.time() - start_time < timeout:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            readings.append(line)
    
    ser.close()
    return readings

def test_dht11_temperature_range():
    """TC-001: Sensor Reads Valid Temperature Range"""
    readings = read_arduino_output()
    
    for reading in readings:
        if "Temperature:" in reading:
            # Extract temp value
            temp = float(reading.split("Temperature: ")[1].split("C")[0])
            assert -40 <= temp <= 80, f"Temp {temp}°C out of range"

def test_dht11_humidity_range():
    """TC-002: Sensor Reads Valid Humidity Range"""
    readings = read_arduino_output()
    
    for reading in readings:
        if "Humidity:" in reading:
            # Extract humidity value
            humidity = float(reading.split("Humidity: ")[1].split("%")[0])
            assert 0 <= humidity <= 100, f"Humidity {humidity}% out of range"

def test_dht11_update_frequency():
    """TC-003: Sensor Updates Every 2 Seconds"""
    readings = read_arduino_output(timeout=10)
    
    # Should get ~5 readings in 10 seconds (1 every 2 sec)
    assert len(readings) >= 4, f"Only got {len(readings)} readings in 10 sec, expected ~5"

if __name__ == "__main__":
    pytest.main([__file__, "-v"])