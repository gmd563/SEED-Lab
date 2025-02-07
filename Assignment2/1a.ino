# Grace Davis
# Assignment 2 - 1a
# This is the arduino code that interpretes the message sent from the python file 1a.py

#include <Wire.h>
#define MY_ADDR 8

// Global variables to be used for I2C communication
volatile uint8_t offset = 0;
volatile uint8_t instruction[32] = {0};
volatile uint8_t msgLength = 0;

void setup() {
  // Set Baud Rate
  Serial.begin(115200);
  
  // Control the built-in LED
  pinMode(LED_BUILTIN, OUTPUT);
  
  // Initialize I2C
  Wire.begin(MY_ADDR);

  // Set callbacks for I2C interrupts
  Wire.onReceive(receive);

}

void loop() {
  // If data on the buffer, read it
  if (msgLength > 0) {

    if (offset == 1) {
      digitalWrite(LED_BUILTIN, instruction[0]);
      }

      printReceived();
      msgLength = 0;
    
  }
}

// printReceived --> helps us see data received from the leader
void printReceived() {

  // Print on serial console
  Serial.print("Offset recieved: ");
  Serial.print("Offset received: ");
  Serial.println(offset);
  Serial.print("Message Length: ");
  Serial.println(msgLength);

  Serial.print("\nString received: ");
  for (int i=0; i < msgLength; i++) {
    Serial.print(" ");
    Serial.print(char(instruction[i]));
    Serial.print("\t");
  }
  
  Serial.println("");

  Serial.print("\nASCII received:  ");
  for (int i=0; i < msgLength; i++) {
    Serial.print(String(instruction[i])+"\t");
  }
  
}

// function called when an I2C interrupt event happens
void receive() {
  
  // Set the offset, this will always be the first byte.
  offset = Wire.read();
  
  // If there is information after the offset, it is telling us more about the command.
  while (Wire.available()) {
    instruction[msgLength] = Wire.read();
    msgLength++;
  }
}
