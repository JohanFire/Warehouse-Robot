import cv2
import numpy
import matplotlib.pyplot as plt

def canny(lane_image):
    gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0) #(image, (kernelSize), deviation)
    canny = cv2.Canny(blur, 50, 150) #(image, lowThreshold, highThreshold)
    
    return canny

image = cv2.imread("test_lane_02.png")
lane_image = numpy.copy(image)

canny = canny(lane_image)

# cv2.imshow('image', canny)
# cv2.waitKey(0)
plt.imshow(canny)
plt.show()