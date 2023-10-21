import cv2

# capture = cv2.VideoCapture(0)
capture = cv2.VideoCapture(1)

if not capture.isOpened():
    print('Not able to open camera.')
    exit()

while True:
    # Capturar un cuadro de la cámara
    ret, frame = capture.read()

    cv2.imshow('Camera', frame)

    # Si presionas la tecla 'q', salir del bucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()