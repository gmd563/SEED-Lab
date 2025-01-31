from smbus2 import SMBus
from time import sleep

ARD_ADDR = 8
i2c = SMBus(1)
offset = 1

while(True):
	string = input(“Enter a string, or 0 to quit: “)
	if string == “0”:
		break
	command = [ord(character) for character in string]
	i2c.write_i2c_block_data(ARD_ADDR, offset, command)
