# Test Case: LCD1602 Display

## TC-003-001: LCD Powers On & Backlight Activates
- **Setup:** Connect LCD to Arduino via I2C (SDA/SCL)
- **Expected:** LCD displays text, backlight is visible
- **Actual:** (describe what you see)
- **Status:** ✓ PASS or ✗ FAIL

## TC-003-002: LCD Displays Temperature Value
- **Setup:** Run `lcd_full_monitor_test.ino`
- **Expected:** Line 1 shows "T: XX.XC" (current temperature)
- **Actual:** (take screenshot of LCD or Serial Monitor)
- **Status:** ✓ PASS or ✗ FAIL

## TC-003-003: LCD Displays Humidity Value
- **Setup:** Monitor LCD output
- **Expected:** Line 1 shows "H: XX%" (current humidity)
- **Actual:** (take screenshot)
- **Status:** ✓ PASS or ✗ FAIL

## TC-003-004: LCD Displays Light Level
- **Setup:** Monitor LCD output
- **Expected:** Line 2 shows "Light: XX%"
- **Actual:** (take screenshot, then cover LDR and verify % drops)
- **Status:** ✓ PASS or ✗ FAIL

## TC-003-005: LCD Updates Every 2 Seconds
- **Setup:** Watch LCD display for 10 seconds
- **Expected:** Temperature/humidity/light values update every 2 seconds
- **Actual:** (count the updates in 10 seconds)
- **Status:** ✓ PASS or ✗ FAIL

## TC-003-006: No Garbage Characters or Corruption
- **Expected:** All text is readable, no overlapping/garbled text
- **Actual:** (describe display quality)
- **Status:** ✓ PASS or ✗ FAIL