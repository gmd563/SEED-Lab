#include <Wire.h>
#define MY_ADDR 8

volatile uint8_t offset = 0;
volatile uint8_t instruction = 0;
volatile uint8_t reply = 0;

void setup() {
  Serial.begin(115200);
  Wire.begin(MY_ADDR);
  Wire.onReceive(receive);
  Wire.onRequest(request);
}

void loop() {
  
}

void receive() {
  offset = Wire.read();
  while(Wire.available()) {
    instruction = Wire.read();
    reply = instruction + 100;
    // instruction = 0;
  }
}

void request() {
  Wire.write(reply);
  reply = 0;
}
