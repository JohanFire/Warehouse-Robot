import cv2

# capture = cv2.VideoCapture(0)
capture = cv2.VideoCapture(1)

if not capture.isOpened():
    print('Not able to open camera.')
    exit()

while True:
    ret, frame = capture.read()

    cv2.imshow('Camera', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()