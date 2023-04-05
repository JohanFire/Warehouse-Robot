# lanes = carriles

import cv2
import numpy

image = cv2.imread("test_lane_01.jpeg")

lane_image = numpy.copy(image)

gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0) #(image, (kernelSize), deviation)

cv2.imshow('image', blur)
cv2.waitKey(0)