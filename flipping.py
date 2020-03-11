# import the necessary packages
import argparse
import cv2
 
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help = "Path to the image")
args = vars(ap.parse_args())
 
# load the image and show it
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
 
# flip the image horizontally
# flipped = cv2.flip(image, 1)
# cv2.imshow("Flipped Horizontally", flipped)

# # flip the image vertically
# flipped = cv2.flip(image, 0)
# cv2.imshow("Flipped Vertically", flipped)
 
# # flip the image along both axes
# flipped = cv2.flip(image, -1)
# cv2.imshow("Flipped Horizontally & Vertically", flipped)

# 1. Question
# Download the source code and images associated with this lesson. Then, use the florida_trip.png to answer the following question.

# Use OpenCV to flip the image horizontally — what is the value of the pixel located at x=259, y=235?
flipped = cv2.flip(image, 1)
(b, g, r) = flipped[235, 259]
print("Pixel at (0, 0) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b))

# 2. Question
# Use the original image from the previous question and flip it horizontally, followed by a 45 degree counter-clockwise rotation, and lastly a vertical flip. What is (approximately) the pixel value located at x=441, y=189?
# flip the image horizontally
(h, w) = image.shape[:2]
(cX, cY) = (w / 2, h / 2)

flipped = cv2.flip(image, 1)

M = cv2.getRotationMatrix2D((cX, cY), 45, 1.0)
flipped = cv2.warpAffine(flipped, M, (w, h))

flipped = cv2.flip(flipped, 0)
(b, g, r) = flipped[189, 441]
print("Pixel at (0, 0) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b))

cv2.imshow("2. Question", flipped)
cv2.waitKey(0)

