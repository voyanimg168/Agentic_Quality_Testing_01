import serial
import time
import re
import pytest
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env
from dotenv import load_dotenv

# Load .env from parent directory (IoT_Arduino_Test/)
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(env_path)

ARDUINO_PORT = os.getenv('ARDUINO_PORT', '/dev/cu.usbmodem21301')

class SerialReader:
    def __init__(self, port=ARDUINO_PORT, baudrate=9600, timeout=2):
        """Initialize serial connection to Arduino"""
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.ser = None
    
    def connect(self):
        """Open serial connection"""
        try:
            self.ser = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
            time.sleep(2)  # Wait for Arduino to reset
            print(f"Connected to Arduino on port {self.port}")
            return True
        except Exception as e:
            print(f"Failed to connect to {self.port}: {e}")
            return False
    
    def read_line(self):
        """Read one line from serial"""
        if self.ser and self.ser.in_waiting > 0:
            return self.ser.readline().decode('utf-8', errors='ignore').strip()
        return None
    
    def read_multiple(self, num_readings=5, timeout=15):
        """Read multiple lines from serial"""
        readings = []
        start_time = time.time()
        
        while len(readings) < num_readings and (time.time() - start_time) < timeout:
            line = self.read_line()
            if line and "Temperature:" in line:
                readings.append(line)
                time.sleep(0.1)
        
        return readings
    
    def close(self):
        """Close serial connection"""
        if self.ser:
            self.ser.close()

class DHT11Validator:
    @staticmethod
    def extract_temperature(reading):
        """Extract temperature from serial reading"""
        match = re.search(r'Temperature: ([\d.]+)', reading)
        return float(match.group(1)) if match else None
    
    @staticmethod
    def extract_humidity(reading):
        """Extract humidity from serial reading"""
        match = re.search(r'Humidity: ([\d.]+)', reading)
        return float(match.group(1)) if match else None
    
    @staticmethod
    def extract_light(reading):
        """Extract light level from serial reading"""
        match = re.search(r'Light: ([\d.]+)', reading)
        return float(match.group(1)) if match else None

# Test Cases
def test_dht11_temperature_range():
    """TC-001: Temperature readings within valid range"""
    reader = SerialReader(port=ARDUINO_PORT)  # Change COM3 to your port
    assert reader.connect(), "Failed to connect to Arduino"
    
    readings = reader.read_multiple(num_readings=5)
    reader.close()
    
    assert len(readings) > 0, "No readings received from Arduino"
    
    for reading in readings:
        temperature = DHT11Validator.extract_temperature(reading)
        assert temperature is not None, f"Could not parse temperature from: {reading}"
        assert -40 <= temperature <= 80, f"Temperature {temperature}°C out of valid range"
    
    print(f"✓ TC-001 PASS: {len(readings)} valid temperature readings")

def test_dht11_humidity_range():
    """TC-002: Humidity readings within valid range"""
    reader = SerialReader(port=ARDUINO_PORT)
    assert reader.connect(), "Failed to connect to Arduino"
    
    readings = reader.read_multiple(num_readings=5)
    reader.close()
    
    for reading in readings:
        humidity = DHT11Validator.extract_humidity(reading)
        assert humidity is not None, f"Could not parse humidity from: {reading}"
        assert 0 <= humidity <= 100, f"Humidity {humidity}% out of valid range"
    
    print(f"✓ TC-002 PASS: {len(readings)} valid humidity readings")

def test_dht11_update_frequency():
    """TC-003: Sensor updates every 2 seconds"""
    reader = SerialReader(port=ARDUINO_PORT)
    assert reader.connect(), "Failed to connect to Arduino"
    
    start = time.time()
    readings = reader.read_multiple(num_readings=5, timeout=15)
    elapsed = time.time() - start
    reader.close()
    
    assert len(readings) >= 4, f"Expected ~5 readings in 15s, got {len(readings)}"
    avg_interval = elapsed / len(readings)
    
    # Should be roughly 2 seconds between readings
    assert 1.5 <= avg_interval <= 3.0, f"Update interval {avg_interval}s not ~2s"
    
    print(f"✓ TC-003 PASS: Update interval {avg_interval:.2f}s")

def test_sensor_consistency():
    """TC-005: Multiple readings show consistent data"""
    reader = SerialReader(port=ARDUINO_PORT)
    assert reader.connect(), "Failed to connect to Arduino"
    
    readings = reader.read_multiple(num_readings=5)
    reader.close()
    
    temperatures = [DHT11Validator.extract_temperature(r) for r in readings]
    temperatures = [t for t in temperatures if t is not None]
    
    # Temperature shouldn't vary wildly between reads
    temperature_range = max(temperatures) - min(temperatures   )
    assert temperature_range < 5, f"Temperature variance {temperature_range}°C too high (sensor unstable?)"
    
    print(f"✓ TC-005 PASS: Temperature stable, variance = {temperature_range:.2f}°C")

if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])