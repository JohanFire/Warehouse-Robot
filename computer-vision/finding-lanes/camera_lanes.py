import cv2
import numpy
import matplotlib.pyplot as plt

def canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0) #(image, (kernelSize), deviation)
    canny = cv2.Canny(blur, 50, 150) #(image, lowThreshold, highThreshold)
    return canny

capture = cv2.VideoCapture(0)
# capture = cv2.VideoCapture(1)
# OpenCV uses 640 x 480 by default, higher makes it slow
# capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
# capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

if not capture.isOpened():
    print('Not able to open camera.')
    exit()

while True:
    ret, frame = capture.read()

    copy_image = numpy.copy(frame)
    canny = canny(copy_image[-1])

    # frame = cv2.resize(frame, (1080, 720))
    cannyResized = cv2.resize(canny,(720,480))

    cv2.imshow('Camera', frame)
    cv2.imshow('canny', cannyResized)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()