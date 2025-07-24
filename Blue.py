import numpy as np
import cv2

image = cv2.imread('image4.png')
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

### Setings
###lower_bound = np.array([H_min, S_min, V_min])
###upper_bound = np.array([H_max, S_max, V_max])

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

### Blue
#lower = np.array([97, 148, 60]) 
#upper = np.array([123, 255, 255])
### New Blue
###lower = np.array([100, 100, 100], np.uint8)
###upper = np.array([140,255,255], np.uint8)
# blue color mas cercano
#lower = np.array([99,115,150])
#upper = np.array([110,255,255])
# define range of blue color in HSV
#lower = np.array([110,50,50])
#upper = np.array([130,255,255])
### con el threshold
lower = np.array([76, 50, 50])
upper = np.array([140, 255, 255])

mask = cv2.inRange(hsv, lower, upper)
result = cv2.bitwise_and(image, image, mask=mask)

while(1):

    cv2.imshow('result', result)

    cv2.imwrite('blue4.png', result)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()

