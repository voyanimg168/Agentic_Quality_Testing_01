#include "DHT.h"
#include <LiquidCrystal_I2C.h>

// DHT11 Setup
#define DHTPIN 2
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

// LDR Setup
#define LDR_PIN A0

// LCD Setup (I2C address 0x27, 16x2 display)
LiquidCrystal_I2C lcd(0x27, 16, 2);

// Buzzer Setup
#define BUZZER_PIN 3
#define TEMP_MIN 18.0
#define TEMP_MAX 28.0

void setup() {
  Serial.begin(9600);
  dht.begin();
  lcd.init();
  lcd.backlight();
  pinMode(BUZZER_PIN, OUTPUT);
  
  // Startup message
  lcd.setCursor(0, 0);
  lcd.print("IoT Monitor");
  lcd.setCursor(0, 1);
  lcd.print("Initializing...");
  
  Serial.println("=== IoT FULL MONITOR TEST ===");
  delay(2000);
  lcd.clear();
}

void loop() {
  // Read DHT11
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();
  
  // Read LDR
  int lightRaw = analogRead(LDR_PIN);
  float lightPercent = (lightRaw / 1023.0) * 100;
  
  // Check for DHT errors
  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("ERROR: DHT11 read failed!");
    lcd.setCursor(0, 0);
    lcd.print("DHT ERROR!");
    digitalWrite(BUZZER_PIN, HIGH);
    delay(500);
    digitalWrite(BUZZER_PIN, LOW);
    delay(1500);
    return;
  }
  
  // Display on LCD (Line 1: Temp/Humidity, Line 2: Light)
  lcd.setCursor(0, 0);
  lcd.print("T:");
  lcd.print(temperature, 1);
  lcd.print("C H:");
  lcd.print(humidity, 0);
  lcd.print("%");
  
  lcd.setCursor(0, 1);
  lcd.print("Light:");
  lcd.print(lightPercent, 0);
  lcd.print("% ");
  
  // Check temperature alarm
  if (temperature < TEMP_MIN || temperature > TEMP_MAX) {
    digitalWrite(BUZZER_PIN, HIGH);  // Sound alarm
    Serial.print("ALERT: Temp ");
    Serial.print(temperature);
    Serial.println("C out of range!");
  } else {
    digitalWrite(BUZZER_PIN, LOW);   // Stop alarm
  }
  
  // Serial output for debugging
  Serial.print("Temp: ");
  Serial.print(temperature);
  Serial.print("C | Humidity: ");
  Serial.print(humidity);
  Serial.print("% | Light: ");
  Serial.print(lightPercent, 0);
  Serial.println("%");
  
  delay(2000);  // Update every 2 seconds
}