# Assignment 2.2b
# Imports
from time import sleep
import numpy as np
import cv2
from cv2 import aruco
import board
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd

# Load image
green = cv2.imread("porsche.jpg")  # Load Pic into OpenCV
greenHSV = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)  # Convert to HSV

# Define green color range
uppergreen = np.array([86, 255, 255])
lowergreen = np.array([36, 50, 50])

# Create mask
mask = cv2.inRange(greenHSV, lowergreen, uppergreen)

kernel = np.ones((5, 5), np.uint8)  # Define 5x5 kernel
for i in range(25):
    # **Apply Erosion**
    mask1 = cv2.erode(mask, kernel, iterations=1)
    # apply dilation
    mask2 = cv2.dilate(mask1, kernel, iterations=1) #apply dilation
    # **Apply Erosion**
    mask3 = cv2.erode(mask2, kernel, iterations=1)
    mask1 = mask3
    i+=1
mask_eroded = mask1
# Bitwise AND to extract green parts
result = cv2.bitwise_and(green, green, mask=mask_eroded)

# Show the result after erosion
#cv2.imshow("Eroded Mask", mask_eroded)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#cv2.imshow("Dilated Mask", mask_dilated)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
cv2.imshow("Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Find contours after erosion
#contour_green_visualize = green.copy()
#contours_green, _ = cv2.findContours(mask_eroded, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours
#cv2.drawContours(contour_green_visualize, contours_green, -1, (0, 255, 0), 3)
#cv2.imshow("Contours", contour_green_visualize)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

# Process contours to find bounding boxes
#greenBox = green.copy()
#greenCenters = np.empty((0, 2))
#greenAreas = np.empty((0))

#for index, cnt in enumerate(contours_green):
#    contour_area = cv2.contourArea(cnt)
#    if contour_area > 300:
#        x, y, w, h = cv2.boundingRect(cnt)
#        center = int(x + w / 2), int(y + h / 2)
#        greenAreas = np.append(greenAreas, contour_area)
#        greenCenters = np.vstack((greenCenters, center))
#        cv2.rectangle(greenBox, (x, y), (x + w, y + h), (0, 0, 255), 2)
#        cv2.putText(greenBox, "green", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
#        cv2.putText(greenBox, "+", center, cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
#
#cv2.imshow("Big Contours", greenBox)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
