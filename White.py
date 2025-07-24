import cv2
import numpy as np

# Load the image
image = cv2.imread('image4.png')

# Convert to HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the white color range in HSV
# Adjust these values based on the specific shades of white in your image
lower_white = np.array([0, 0, 200])  # Example: low saturation, high value
upper_white = np.array([255, 25, 255]) # Example: low saturation, high value

# New white
#lower_white = np.array([0, 0, 212])
#upper_white = np.array([131, 255, 255])

# Create a mask for the white regions
mask = cv2.inRange(hsv_image, lower_white, upper_white)

# Define the replacement color (e.g., red)
replacement_color_bgr = [36, 255, 12] # Red in BGR format

# Create an image filled with the replacement color
replacement_image = np.full_like(image, replacement_color_bgr)

# Apply the mask to the replacement color image
replaced_regions = cv2.bitwise_and(replacement_image, replacement_image, mask=mask)

# Invert the mask to get everything except the white regions
inverted_mask = cv2.bitwise_not(mask)

# Get the original image without the white regions
original_without_white = cv2.bitwise_and(image, image, mask=inverted_mask)

# Combine the original image (without white) with the replaced regions
final_image = cv2.add(original_without_white, replaced_regions)

while True:

# Display or save the result
    ###cv2.imshow('Original Image', image)
    ###cv2.imshow('Final Image', final_image)
    cv2.imshow('Mask White', mask)
    cv2.imwrite('white4.png', mask)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cv2.waitKey(0)
cv2.destroyAllWindows()
