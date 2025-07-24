### This script filters only the blue color from an RGB image.
import numpy as np
import cv2

image = cv2.imread('path from your image')
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

### Setings HSV
###lower_bound = np.array([H_min, S_min, V_min])
###upper_bound = np.array([H_max, S_max, V_max])

### Blue threshold
lower = np.array([76, 50, 50])
upper = np.array([140, 255, 255])

mask = cv2.inRange(hsv, lower, upper)
result = cv2.bitwise_and(image, image, mask=mask)

while(1):

    cv2.imshow('result', result)
    cv2.imwrite('blue.png', result)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()

