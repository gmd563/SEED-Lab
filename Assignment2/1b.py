from smbus2 import SMBus
from time import sleep
import board
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd

lcdCols = 16
lcdRows = 2

i2c1 = board.I2C()
lcd = character_lcd.Character_LCD_RGB_I2C(i2c1, lcdCols, lcdRows)
lcd.clear()
lcd.color = [0, 0, 100]
lcd.text_direction = lcd.LEFT_TO_RIGHT

ARD_ADDR = 8
i2c2 = SMBus(1)
offset = 1

while(True):
    command = int(input("Enter an integer between 0 and 100, or 0 to quit: "))
    lcd.clear()
    if command == 0:
        break
    elif 0 < command < 100:
        i2c2.write_byte_data(ARD_ADDR, offset, command)
        sleep(0.1)
        reply = i2c2.read_byte_data(ARD_ADDR, offset)
        lcd.message = str(reply)
        print("Received from Arduino: " + str(reply))
    else:
        print("Invalid Input.")
