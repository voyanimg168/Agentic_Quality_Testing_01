#define LDR_PIN A0  // Analog pin for light sensor

void setup() {
  Serial.begin(9600);
  Serial.println("LDR Light Sensor Test Starting...");
}

void loop() {
  int lightValue = analogRead(LDR_PIN);
  
  // Convert to percentage (0-1023 becomes 0-100%)
  float lightPercent = (lightValue / 1023.0) * 100;
  
  Serial.print("Light Level: ");
  Serial.print(lightValue);
  Serial.print(" (");
  Serial.print(lightPercent);
  Serial.println("%)");
  
  delay(1000);  // Read every 1 second
}