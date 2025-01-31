#imports
from time import sleep
import numpy as np
import cv2
from cv2 import aruco
import board
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd

#Aruco Dictionary
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_6X6_50)
lcd_columns = 16
lcd_rows = 2
i2c = board.I2C()
lcd = character_lcd.Character_LCD_RGB_I2C(i2c, lcd_columns,lcd_rows)
lcd.clear()
lcd.color = [200,0,200] #purple

camera = cv2.VideoCapture(0)

#loop
while True:
    ret,image = camera.read()
    sleep(.5)
    grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #Detect Aruco Markers and show on popup images
    corners,ids,rejected = aruco.detectMarkers(grey,aruco_dict)
    overlay = cv2.cvtColor(grey,cv2.COLOR_GRAY2RGB)
    overlay = aruco.drawDetectedMarkers(overlay,corners,borderColor = 4)
    if not ids is None:
        ids = ids.flatten()
        for (outline, id) in zip(corners, ids):
            markerCorners = outline.reshape((4,2))
            overlay = cv2.putText(overlay, str(id),(int(markerCorners[0,0]), int(markerCorners[0,1]) - 15),cv2.FONT_HERSHEY_SIMPLEX,0.5, (255,0,0), 2)
        cv2.imshow("overlay",overlay)
        lcd.clear()
        lcd.message=str(ids)                                              
    else:
        lcd.clear()
        lcd.message="No Markers Found"
    cv2.imshow("overlay",overlay)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break
camera.release()
cv2.destroyAllWindows

