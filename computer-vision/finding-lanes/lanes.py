import cv2
import numpy
import matplotlib.pyplot as plt
from icecream import ic

def canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0) #(image, (kernelSize), deviation)
    canny = cv2.Canny(blur, 50, 150) #(image, lowThreshold, highThreshold)
    return canny

def display_lines(image, lines):
    """ line_image is an array of zeros with the same shape as the lane images array"""
    line_image =numpy.zeros_like(image)
    
    if lines is not None:
        for line in lines:
            ic(line)
            """ each line is a 2D array containing line coordinates [[x1, y1, x2, y2]] 
            now will reshape every line into a 1D array [x1, y1, x2, y2]
            """
            # line = line.reshape(4)
            x1, y1, x2, y2 = line.reshape(4)

            # draw line
            """ args(line_image, (first point of the line), (second point)), color, thickness """
            cv2.line(line_image, (x1, y1), (x2, y2), (255, 0 ,0), 10)
    
    return line_image

def region_of_interest(image):
    """ will return the enclosed region of our field of view and recall that the enclosed region was triangular in shape """
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
    
    # will return only the region of interest traced by the polygonal contour of the mask
    masked_image = cv2.bitwise_and(image, mask) 

    return masked_image

# ic.disable()

image = cv2.imread("test_lane_02.png")
lane_image = numpy.copy(image)
canny_image = canny(lane_image)
cropped_image = region_of_interest(canny_image)

""" 2nd & 3rd arguments are really important 
as they specify the size of the bits, 
Rho = distance resolution of the accumulator in pixels
Theta = angle resolution of the accumulator in radians

arguments:
- image
- Precision of 2 pixels
- 1 degree precision (1 degree = pi/180)
- threshold = 100 forth
# Threshold: minimum number of votes/intersections needed to accept a candidate line
- placeholder empty array
- minimum length of a line in pixels we will accept into the output
- max line gap 
"""
lines = cv2.HoughLinesP(
    cropped_image, 
    2, 
    numpy.pi/180, 100, 
    numpy.array([]),
    minLineLength=40,
    maxLineGap=5
) 
line_image = display_lines(lane_image, lines)
combo_image = cv2.addWeighted(lane_image, 0.8, line_image, 1, 1) 


""" For show """
lane_imageResized = cv2.resize(lane_image,(720,480))
canny_imageResized = cv2.resize(canny_image,(720,480))
cropped_imageResized = cv2.resize(cropped_image,(720,480))
line_imageResized = cv2.resize(line_image,(720,480)) 

cv2.imshow('lane_image', lane_imageResized)
cv2.imshow('canny', canny_imageResized)
cv2.imshow('region_of_interest', cropped_imageResized)
cv2.imshow('lines', line_imageResized)
cv2.imshow('RESULT', combo_image)

cv2.waitKey(0)

# plt.imshow(canny)
# plt.show()