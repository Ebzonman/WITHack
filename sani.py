import  numpy as np
import cv2

hLower = 0
sLower = 0 
vLower = 20
hUpper = 180 
sUpper = 255 
vUpper = 38
#Put these values into an array, this will be helpful when passing it to functions later
lowerRange = (hLower, sLower, vLower)
upperRange = (hUpper, sUpper, vUpper)


cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    colourFilter = cv2.inRange(frame, lowerRange, upperRange) 
    cv2.imshow('filtered', colourFilter)
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
       break

cap.release()
cv2.destroyAllWindows()




       
