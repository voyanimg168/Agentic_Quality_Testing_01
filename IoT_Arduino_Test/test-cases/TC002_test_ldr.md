# Test Case: LDR Light Sensor

## TC-LDR-001: Sensor Reads Valid Light Range
- **Expected:** Values between 0 and 1023 (8-bit ADC)
- **Actual:** (paste Serial Monitor output)
- **Status:** ✓ PASS or ✗ FAIL

## TC-LDR-002: Sensor Detects Light Decrease
- **Setup:** Place LDR in bright room
- **Action:** Cover LDR with hand
- **Expected:** Light value decreases by at least 100 points
- **Actual:** (show before/after readings)
- **Status:** ✓ PASS or ✗ FAIL

## TC-LDR-003: Sensor Detects Light Increase
- **Setup:** Cover LDR in dark box
- **Action:** Shine flashlight on it
- **Expected:** Light value increases by at least 100 points
- **Actual:** (show before/after readings)
- **Status:** ✓ PASS or ✗ FAIL

## TC-LDR-004: Sensor Updates Every 1 Second
- **Expected:** New reading printed every 1 second
- **Actual:** (count readings in 10 seconds)
- **Status:** ✓ PASS or ✗ FAIL