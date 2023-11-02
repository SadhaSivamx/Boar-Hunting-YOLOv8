int ledPin = 13; // Define the LED pin as pin 13

void setup() {
  pinMode(ledPin, OUTPUT); // Set the LED pin as an output
  Serial.begin(9600); // Initialize serial communication
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read(); // Read the command from PySerial
    
    if (command == '1') {
      digitalWrite(ledPin, HIGH); // Turn on the LED
      Serial.println("LED is ON");
      delay(1000);
       digitalWrite(ledPin, LOW); 
    }
  }
}
