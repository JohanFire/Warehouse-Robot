import cv2
import numpy
import matplotlib.pyplot as plt
from icecream import ic

def canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0) #(image, (kernelSize), deviation)
    canny = cv2.Canny(blur, 50, 150) #(image, lowThreshold, highThreshold)
    return canny

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

def make_coordinates(image, line_parameters):
    """ return value that denotes X and Y coordinates of the line. \n
    ``y = mx + b`` \n
    where x = (y-b) / m \n
    """
    slope, intercept = line_parameters
    
    ic(image.shape)
    """
    image.shape: (704, 1279, 3)
    image.shape: (height, width, numberOfChannels)
    """ 

    y1 = image.shape[0]
    y2 = int(y1 * (3/5))

    x1 = int((y1 - intercept)/slope)
    x2 = int((y2 - intercept)/slope)

    return numpy.array([x1, y1, x2, y2])

def average_slop_intercept(image, lines):
    """ calculate the slope(pendiente)
    ---
    ``y = mx + b`` \n
    where m = (y2-y1) / (x2-x1) \n
    b = y - mx
    """
    left_fit = []
    right_fit = []

    for line in lines:
        x1, y1, x2, y2 = line.reshape(4)
        
        """ polyfit will a first degree polynomial which would simply be a linear function of Y is equal to MX plus B,
        and its going to fit this polynomial to our X&Y points and return a vector of coefficients which describe the slope and Y intercept """
        parameters = numpy.polyfit((x1, x2), (y1, y2), 1)
        ic(parameters)

        slope = parameters[0]
        intercept = parameters[1]

        """ determine if the slope of the line corresponds to the left or right line """
        if slope < 0:
            left_fit.append((slope, intercept))
        else:
            right_fit.append((slope, intercept))
    
    ic(left_fit)
    ic(right_fit)

    left_fit_average = numpy.average(left_fit, axis=0)
    right_fit_average = numpy.average(right_fit, axis=0)

    ic(left_fit_average, right_fit_average)

    left_line = make_coordinates(image, left_fit_average)
    right_line = make_coordinates(image, right_fit_average)

    return numpy.array([left_line, right_line])

def main_image():
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
    averaged_lines = average_slop_intercept(lane_image, lines)
    line_image = display_lines(lane_image, lines)
    combo_image = cv2.addWeighted(lane_image, 0.8, line_image, 1, 1) 

    average_line_image = display_lines(lane_image, averaged_lines)
    average_combo_image = cv2.addWeighted(lane_image, 0.8, average_line_image, 1, 1)


    """ Resized images, for show """
    lane_imageResized = cv2.resize(lane_image,(720,480))
    canny_imageResized = cv2.resize(canny_image,(720,480))
    cropped_imageResized = cv2.resize(cropped_image,(720,480))
    line_imageResized = cv2.resize(line_image,(720,480)) 
    averaged_line_imageResized = cv2.resize(average_line_image,(720,480)) 
    # combo_imageResized = cv2.resize(combo_image, (720, 480))

    cv2.imshow('lane_image', lane_imageResized)
    cv2.imshow('canny', canny_imageResized)
    cv2.imshow('region_of_interest', cropped_imageResized)
    cv2.imshow('lines', line_imageResized)
    cv2.imshow('averaged_line', averaged_line_imageResized)
    # cv2.imshow('display lane lines', combo_imageResized)
    cv2.imshow('RESULT', average_combo_image)

    cv2.waitKey(0)

    # plt.imshow(canny)
    # plt.show()

def main():
    cap = cv2.VideoCapture('test2.mp4')
    while(cap.isOpened()):
        _, frame = cap.read()

        canny_image = canny(frame)
        cropped_image = region_of_interest(canny_image)
        lines = cv2.HoughLinesP(
            cropped_image, 
            2, 
            numpy.pi/180, 100, 
            numpy.array([]),
            minLineLength=40,
            maxLineGap=5
        )
        averaged_lines = average_slop_intercept(frame, lines)
        line_image = display_lines(frame, lines)
        combo_image = cv2.addWeighted(frame, 0.8, line_image, 1, 1) 

        # draw the middle line between left & right lane
        middle_line_coordinates = [averaged_lines[1][0] - averaged_lines[0][0], (averaged_lines[1][2] + averaged_lines[0][2])/2]

        average_line_image = display_lines(frame, averaged_lines)
        average_combo_image = cv2.addWeighted(frame, 0.8, average_line_image, 1, 1)

        reference_line = cv2.line(average_combo_image, (640, 560), (640, 720), (0, 255 ,0), 3)
        middle_line = cv2.line(average_combo_image, (int(middle_line_coordinates[1]), 432), (middle_line_coordinates[0], 720), (255, 0 ,0), 3)

        """ Resized images, for show """
        # frameResized = cv2.resize(frame,(720,480))
        # cv2.imshow('RESULT', average_combo_image)

        # cv2.imshow('RESULT', combo_image)
        cv2.imshow('RESULT', average_combo_image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
