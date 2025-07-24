### This script filters only the orange color from an RGB image
import numpy as np
import cv2

image = cv2.imread('image4.png')
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

### Orange
#lower = np.array([10, 75, 20])
#upper = np.array([23, 252, 255])
### RGB Orange 255,128,0
### New Orange
###lower = (0, 13, 125)
###upper = (18, 255, 255)
lower = (0, 200, 50)
upper = (15, 255, 255)
# Orange range
#lower = np.array([11, 43, 46])
#upper = np.array([25, 255, 255])
#lower = np.array([10, 100, 20])
#upper = np.array([25, 255, 255])

'''
### Red
lower1 = np.array([0, 188, 117])
upper1 = np.array([9, 255, 255])
lower2 = np.array([172, 175, 109])
upper2 = np.array([179, 255, 255])

mask1 = cv2.inRange(hsv, lower1, upper1)
mask2 = cv2.inRange(hsv, lower2, upper2)
mask = cv2.add(mask1, mask2)
result = cv2.bitwise_and(image, image, mask= mask)
'''

mask = cv2.inRange(hsv, lower, upper)
result = cv2.bitwise_and(image, image, mask=mask)

while True:

    cv2.imshow('result', result)

    cv2.imwrite('orange4.png', result)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cv2.waitKey(0)
cv2.destroyAllWindows()

