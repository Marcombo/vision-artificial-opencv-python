import cv2

color = (0, 255, 255)
grosor = 2

clasificador = cv2.CascadeClassifier('../haarcascades/haarcascade_frontalface_default.xml')

camara = cv2.VideoCapture(0)
if not camara.isOpened():
    print("No es posible abrir la cámara")
    exit()

while True:
    ret, frame = camara.read()
    if not ret:
        print("No es posible obtener la imagen")
        break
    frame_byn = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    caras = clasificador.detectMultiScale(frame_byn)
    for (x, y, ancho, alto) in caras:
        cv2.rectangle(frame,(x, y),(x + ancho, y + alto),color, grosor)

    cv2.imshow('webcam', frame)
    
    if cv2.waitKey(1) == ord('q'): break

camara.release()
cv2.destroyAllWindows()

