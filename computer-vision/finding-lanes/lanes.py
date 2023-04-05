# lanes = carriles

import cv2
import numpy

image = cv2.imread("test_lane_01.jpeg")

# create a copy of original image
lane_image = numpy.copy(image)

# create grayscale of the color image
gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)

cv2.imshow('image', gray)
cv2.waitKey(0)