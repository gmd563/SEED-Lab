import cv2
import numpy as np

def detect_green_shape():
    # Open the camera
    camera = cv2.VideoCapture(0)
    
    if not camera.isOpened():
        print("Error: Could not open camera.")
        return
    
    while True:
        # Capture frame
        ret, frame = camera.read()
        if not ret:
            print("Failed to grab frame")
            break
        
        # Convert to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # Define green color range
        lower_green = np.array([36, 50, 50])
        upper_green = np.array([86, 255, 255])
        
        # Create mask
        mask = cv2.inRange(hsv, lower_green, upper_green)
        
        # Define kernel for morphological transformations
        kernel = np.ones((5, 5), np.uint8)
        
        # Apply morphological transformations
        mask = cv2.erode(mask, kernel, iterations=2)  # Erosion to remove noise
        mask = cv2.dilate(mask, kernel, iterations=2)  # Dilation to restore shape
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=2)  # Close gaps
        
        # Find contours
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        # Draw contours on the original frame
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 500:  # Ignore small areas
                cv2.drawContours(frame, [contour], -1, (0, 255, 0), 3)
        
        # Show the processed frames
        cv2.imshow("Green Mask", mask)
        cv2.imshow("Detected Green Shape", frame)
        
        # Exit condition
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release resources
    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_green_shape()
