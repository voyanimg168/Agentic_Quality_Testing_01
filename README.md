# IoT Environmental Monitor — QA Testing Project

## Overview

Arduino-based temperature, humidity, and light sensor project with comprehensive QA test cases and Python-based test automation.

## Project Structure

- `arduino-code/` — Arduino sketch files (.ino)
- `test-cases/` — Manual QA test cases (markdown)
- `tests/` — Automated Python test validation (pytest)
- `circuit-diagrams/` — Wiring diagrams for each sensor
- `bug-log.md` — Issues found during testing

## Getting Started

### Hardware Setup

1. Order LAFVIN Project Super Starter Kit ($31)
2. Follow circuit diagrams in `circuit-diagrams/`
3. Connect Arduino to laptop via USB

### Software Setup

```bash
source venv/bin/activate
pip install -r requirements.txt
```

### Upload Code

1. Open `arduino-code/dht11_test.ino` in Arduino IDE
2. Install Adafruit DHT library
3. Upload to Arduino

### Run Tests

**Manual (Serial Monitor):**

- Open Serial Monitor in Arduino IDE
- Verify TC-001 through TC-004 PASS

**Automated (Python):**

```bash
pytest tests/ -v
```

## Test Cases

- [TC-001-DHT11](test-cases/TC-001-DHT11.md) — Temperature/humidity sensor
- [TC-002-LDR](test-cases/TC-002-LDR.md) — Light sensor
- [TC-003-LCD](test-cases/TC-003-LCD.md) — Display
- [TC-004-BUZZER](test-cases/TC-004-BUZZER.md) — Alarm

## Bug Log

See [bug-log.md](bug-log.md) for issues discovered.
