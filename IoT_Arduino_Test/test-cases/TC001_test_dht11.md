# Test Case: DHT11 Temperature Sensor

## TC-001: Sensor Reads Valid Temperature Range

- **Expected:** Temperature between -40°C and 80°C
- **Actual:** (paste your Serial Monitor output)
- **Status:** ✓ PASS or ✗ FAIL

## TC-002: Sensor Reads Valid Humidity Range

- **Expected:** Humidity between 0% and 100%
- **Actual:** (paste your Serial Monitor output)
- **Status:** ✓ PASS or ✗ FAIL

## TC-003: Sensor Updates Every 2 Seconds

- **Expected:** New reading printed every 2 seconds
- **Actual:** (count the readings in 10 seconds)
- **Status:** ✓ PASS or ✗ FAIL

## TC-004: Error Handling — No Sensor Connected

- **Expected:** "ERROR: Failed to read" message
- **Actual:** (unplug DHT11, watch Serial Monitor)
- **Status:** ✓ PASS or ✗ FAIL
