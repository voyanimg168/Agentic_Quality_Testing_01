# Test Case: Buzzer Alarm

## TC-004-001: Buzzer Stays Silent in Normal Range

- **Setup:** Room temperature is 18-28°C
- **Expected:** Buzzer makes NO sound during normal operation
- **Actual:** (listen for sound, confirm none)
- **Status:** ✓ PASS or ✗ FAIL

## TC-004-002: Buzzer Sounds When Temperature Too Low

- **Setup:** Place DHT11 in cold environment (fridge/freezer)
- **Expected Temperature:** Below 18°C
- **Expected:** Buzzer sounds continuously
- **Actual:** (describe buzzer behavior)
- **Duration:** (how long does it sound?)
- **Status:** ✓ PASS or ✗ FAIL

## TC-004-003: Buzzer Sounds When Temperature Too High

- **Setup:** Place DHT11 near heat source (lamp/heater)
- **Expected Temperature:** Above 28°C
- **Expected:** Buzzer sounds continuously
- **Actual:** (describe buzzer behavior)
- **Status:** ✓ PASS or ✗ FAIL

## TC-004-004: Buzzer Stops When Temperature Returns to Normal

- **Setup:** Temperature goes out of range, then returns to 18-28°C
- **Expected:** Buzzer stops immediately when temp normalizes
- **Actual:** (test this scenario)
- **Status:** ✓ PASS or ✗ FAIL

## TC-004-005: Buzzer Activates on DHT11 Error

- **Setup:** Disconnect DHT11 sensor
- **Expected:** Buzzer sounds and LCD shows "DHT ERROR!"
- **Actual:** (describe behavior)
- **Status:** ✓ PASS or ✗ FAIL

## TC-004-006: Buzzer Sound Quality

- **Expected:** Clear, audible beep (minimum 80dB)
- **Actual:** (describe tone/volume)
- **Status:** ✓ PASS or ✗ FAIL
