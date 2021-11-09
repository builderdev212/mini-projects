#include <ESP8266WiFi.h>

const char *ssid = "";
const char *password = "";

int value = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(2, OUTPUT);
  digitalWrite(2, LOW);
  delay(10);

  // Explicitly set the ESP8266 to be a WiFi-client
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }
  delay(10);
}

void loop() {
  digitalWrite(2, HIGH);
  delay(10);
  value = analogRead(A0);
  digitalWrite(2, LOW);

  Serial.println(value);
  delay(1000);
}
