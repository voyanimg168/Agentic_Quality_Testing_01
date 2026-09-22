#include "DHT.h"

#define DHTPIN 2           // DHT11 data pin
#define DHTTYPE DHT11      // DHT 11
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
  Serial.println("DHT11 Sensor Test Starting...");
}

void loop() {
  delay(2000);  // Read every 2 seconds
  
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();
  
  // Check if reads failed
  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("ERROR: Failed to read from DHT sensor!");
    return;
  }
  
  Serial.print("Humidity: ");
  Serial.print(humidity);
  Serial.print("%  Temperature: ");
  Serial.print(temperature);
  Serial.println("C");
}