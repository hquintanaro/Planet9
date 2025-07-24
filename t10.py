### detect-and-visualize-differences-between-two-images-with-opencv-python
### second example
from skimage.metrics import structural_similarity as ssim
import imutils
import cv2

imageA = cv2.imread("image_example1")
imageB = cv2.imread("image_example2")

grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

# Compute SSIM between the two images
###(score, diff) = compare_ssim(grayA, grayB, full=True)
(score, diff) = ssim(grayA, grayB, full=True)
print("Image Similarity: {}".format(score * 100))

# The diff image contains the actual image differences between the two images
# and is represented as a floating point data type in the range [0,1]
# so we must convert the array to 8-bit unsigned integers in the range
# [0,255] before we can use it with OpenCV
diff = (diff * 255).astype("uint8")
diff_box = cv2.merge([diff, diff, diff])

# Threshold the difference image, followed by finding contours to
# obtain the regions of the two input images that differ
thresh = cv2.threshold(diff, 0, 255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

for c in cnts:

    (x, y, w, h) = cv2.boundingRect(c)
    cv2.rectangle(imageA, (x, y), (x + w, y + h), (36, 255, 12), 2)
    cv2.rectangle(imageB, (x, y), (x + w, y + h), (36, 255, 12), 2)
    cv2.rectangle(diff_box, (x, y), (x + w, y + h), (36,255,12), 2)

while True:

    # Display the images with annotated differences
    cv2.imshow("Before", imageA)
    cv2.imshow("After", imageB)
    cv2.imshow('diff_box', diff_box)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cv2.waitKey(0)
cv2.destroyAllWindows()
