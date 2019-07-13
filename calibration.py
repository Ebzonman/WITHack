# Contour Test Platform
# Import Relevant Libraries
import cv2
import numpy as np
import time

point = []
minHue = 0
maxHue = 0
minSat = 0
maxSat = 0
minVal = 0
maxVal = 0

def mouse_click(event, x, y, flags, param):

	# If the left mouse button is clicked...
	global minHue, maxHue, minSat, maxSat, minVal, maxVal
	if event == cv2.EVENT_LBUTTONDOWN:

		point = [x, y]
		# print(f'Point Coordinates: {x} x {y}')
		# print(f'HSV Values at Point: {hsv[y,x]}')
		currentHue = hsv[y,x][0]
		currentSat = hsv[y,x][1]
		currentVal = hsv[y,x][2]
		print(f'H:{currentHue} | S:{currentSat} | V:{currentVal}')
		if minHue == 0:
			minHue = currentHue
			maxHue = currentHue
			minSat = currentSat
			maxSat = currentSat
			minVal = currentVal
			maxVal = currentVal

		if currentHue < minHue:
			minHue = currentHue
		elif currentHue > maxHue:
			maxHue = currentHue
		if currentSat < minSat:
			minSat = currentSat
		elif currentSat > maxSat:
			maxSat = currentSat
		if currentVal < minVal:
			minVal = currentVal
		elif currentVal > maxVal:
			maxVal = currentVal


def loopVideo(cap, videoName):
    ret, frame = cap.read()
    if ret == False:
        print("done")
        cap.release()
        cap = cv2.VideoCapture(videoName)
        ret, frame = cap.read()
    return frame, cap

# Request the Device to Capture Footage from Camera
# Setting it to  video or not
cap = cv2.VideoCapture(0)
#video = cv2.VideoCapture("ObstacleTest1.avi")

cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame", mouse_click)

while(True):
    _, frame = cap.read()
   # frame, video = loopVideo(video, "ObstacleTest1.avi")

    # Obtaining the Number of Rows and Columns in the Image
    rows, cols = frame.shape[:2]

    # Small Blur to Make Masking More Consistent
    blur = cv2.GaussianBlur(frame, (3,3), 0)

    # Convert the Image to HSV Colourspace
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    # Filtering the Hue
    mask_Colour = cv2.inRange(hsv, np.array([minHue, minSat, minVal]), np.array([maxHue, maxSat, maxVal]))

    kernel = np.ones((3,3), np.uint8)
    # Apply Morphological Opening to Make Contours Better Defined
    mask_Colour = cv2.morphologyEx(mask_Colour, cv2.MORPH_OPEN, kernel)

    # Find Contours for the Specified Mask
    contours, _ = cv2.findContours(mask_Colour, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Draw the contours
    cv2.drawContours(frame, contours, -1, (0,255,0), 3)

    # Show the Frames
    cv2.imshow('Frame', frame)
    cv2.imshow('Colour Mask', mask_Colour)

    # If the key 'q' is pressed, exit the program.
    if cv2.waitKey(5) & 0xFF == ord('q'):
	    break

    # Slows down the replay
    time.sleep(0.05)

print(f'Range1 | {minHue}:{minSat}:{minVal}')
print(f'Range2 | {maxHue}:{maxSat}:{maxVal}')

# End Video Capture and Close Opened Windows
video.release()
cv2.destroyAllWindows()