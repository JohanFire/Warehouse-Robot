import cv2
import numpy as np

capture = cv2.VideoCapture(1)

while (capture.isOpened()):
    _, frame = capture.read()

    if (cv2.waitKey(1) == ord('s')):
        break

    qrDetector = cv2.QRCodeDetector()
    data, bbox, rectifiedImage = qrDetector.detectAndDecode(frame)

    if len(data) > 0:
        print(f'Data: {data}')
        cv2.imshow('webcam', rectifiedImage)
    else:
        cv2.imshow('webcam', frame)

capture.release()
cv2.destroyAllWindows()
