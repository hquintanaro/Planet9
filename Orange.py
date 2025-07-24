### This script filters only the orange color from an RGB image
import numpy as np
import cv2

image = cv2.imread('image4.png')
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

### Orange range threshold
lower = (0, 200, 50)
upper = (15, 255, 255)

mask = cv2.inRange(hsv, lower, upper)
result = cv2.bitwise_and(image, image, mask=mask)

while True:

    cv2.imshow('result', result)
    cv2.imwrite('orange.png', result)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cv2.waitKey(0)
cv2.destroyAllWindows()

