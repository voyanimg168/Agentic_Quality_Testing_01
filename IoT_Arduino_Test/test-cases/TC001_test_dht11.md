# Test Case: DHT11 Temperature Sensor

## TC-001: Sensor Reads Valid Temperature Range

- **Expected:** Temperature between -40°C and 80°C
- **Actual:**
  DHT1 36.00% Temperature: 28.10C
  Humidity: 36.00% Temperature: 27.80C
  DHT11 Sensor Test Starting...
  Humidity: 36.00% Temperature: 27.80C
  Humidity: 36.00% Temperature: 27.80C
  Humidity: 36.00% Temperature: 27.80C
  Humidity: 36.00% Temperature: 27.80C
  Humidity: 36.00% Temperature: 27.80C
  Humidity: 36.00% Temperature: 27.80C
  Humidity: 36.00% Temperature: 27.80C
  Humidity: 36.00% Temperature: 27.80C
  Humidity: 36.00% Temperature: 27.80C
- **Status:** [✓ PASS] or ✗ FAIL

## TC-002: Sensor Reads Valid Humidity Range

- **Expected:** Humidity between 0% and 100%
- **Actual:**
  DHT1 36.00% Temperature: 28.10C
  Humidity: 36.00% Temperature: 27.80C
  DHT11 Sensor Test Starting...
  Humidity: 36.00% Temperature: 27.80C
  Humidity: 36.00% Temperature: 27.80C
  Humidity: 36.00% Temperature: 27.80C
  Humidity: 36.00% Temperature: 27.80C
  Humidity: 36.00% Temperature: 27.80C
  Humidity: 36.00% Temperature: 27.80C
  Humidity: 36.00% Temperature: 27.80C
  Humidity: 36.00% Temperature: 27.80C
  Humidity: 36.00% Temperature: 27.80C
- **Status:** [✓ PASS] or ✗ FAIL

## TC-003: Sensor Updates Every 2 Seconds

- **Expected:** New reading printed every 2 seconds
- **Actual:** (count the readings in 10 seconds (not 2) => change delay(2000) to delay(10,000))
  Humidity: 31.00% Temperature: 28.40C
  Humidity: 31.00% Temperature: 28.30C
  Humidity: 31.00% Temperature: 28.30C
  Humidity: 31.00% Temperature: 28.50C
  Humidity: 31.00% Temperature: 28.50C
  Humidity: 31.00% Temperature: 28.50C
  Humidity: 31.00% Temperature: 28.50C
- **Status:** [✓ PASS] or ✗ FAIL

## TC-004: Error Handling — No Sensor Connected

- **Expected:** "ERROR: Failed to read" message
- **Actual:** (unplug DHT11, watch Serial Monitor)
  OS error: cannot open port /dev/cu.usbmodem21301: No such file or directory
  Error: unable to open port /dev/cu.usbmodem21301 for programmer arduino

Failed uploading: uploading error: exit status 1
Port monitor error: command 'open' failed: no such file or directory. Could not connect to /dev/cu.usbmodem21301 serial port.

- **Status:** ✓ PASS or [✗ FAIL]
