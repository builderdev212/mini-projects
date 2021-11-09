void setup()
{
  // define pin modes
  for (int pin=2; pin < 14; ++pin) {
    pinMode(pin, OUTPUT);
  }
}

void loop() 
{
  int switchState = digitalRead(13);
  
  if (switchState == HIGH) {
    for (int pin=2; pin < 12; ++pin) {
      int buttonState = digitalRead(12);
      if (buttonState == HIGH) {
        break; 
      }
      digitalWrite(pin, HIGH);
      delay(100);
    }
    int buttonState = digitalRead(12);
    if (buttonState == HIGH) {
    } else {
      for (int pin=2; pin < 12; ++pin) {
        int buttonState = digitalRead(12);
        if (buttonState == HIGH) {
          break; 
        }
        digitalWrite(pin, LOW);
        delay(100);
      }
    }
    for (int pin=2; pin < 12; ++pin) {
      digitalWrite(pin, LOW);
    }
  } else {
    delay(10);
  }
}
