import cv2
import numpy
import matplotlib.pyplot as plt

def canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0) #(image, (kernelSize), deviation)
    canny = cv2.Canny(blur, 50, 150) #(image, lowThreshold, highThreshold)
    return canny

# will return the enclosed region of our field of view and recall that the enclosed region was triangular in shape
def region_of_interest(image):
    # this sizes corresponds to the triangle I drew before in matplotlib
    # camn array is 2-dimensional: (m, n)
    height = image.shape[0]

    # set the tringle polygon in an array of polygon
    polygons = numpy.array([
        [(200, height), (1100, height), (550, 250)]
        ])

    # then apply this triangle polygon to a black mask with same dimension
    mask = numpy.zeros_like(image)

    cv2.fillPoly(mask, polygons, 255) # color of polygon, completely white
    
    return mask

image = cv2.imread("test_lane_02.png")
lane_image = numpy.copy(image)

canny = canny(lane_image)

cv2.imshow('image', region_of_interest(canny))
cv2.waitKey(0)
# plt.imshow(canny)
# plt.show()