#include <Wire.h>
#define MY_ADDR 8

volatile uint8_t offset = 0;
volatile uint8_t instruction[100] = {0};
volatile uint8_t msgLength = 0;

void setup() {
	Serial.begin(115200);
	Wire.begin(MY_ADDR);
	Wire.onReceive(receive);
}

void loop() {
	if (msgLength > 0) {
		printReceived();
		msgLength = 0;
	}
}

void printReceived() {
	Serial.print(“Instruction received (ASCII): “);
	for (int i = 0; i < msgLength; i++) {
		Serial.print(instruction[i] + ”\t”);
	}
	Serial.println(“”);

	Serial.print(“Instruction received (String): “);
	for (int i = 0; i < msgLength; i++) {
		Serial.print((char)instruction[i]);
	}
	Serial.println(“”);
}

void receive() {
	offset = Wire.read();
	while (Wire.available()) {
		instruction[msgLength] = Wire.read();
		msgLength++;
	}
}
