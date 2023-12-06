import cv2

# capture = cv2.VideoCapture(0)
# capture = cv2.VideoCapture(1)
capture = cv2.VideoCapture('http://192.168.193.97:8080/video')
# OpenCV uses 640 x 480 by default, higher makes it slow
# capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
# capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

if not capture.isOpened():
    print('Not able to open camera.')
    exit()

while True:
    ret, frame = capture.read()

    # frame = cv2.resize(frame, (1080, 720))
    cv2.imshow('Camera', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()