import cv2

sombrero = cv2.imread('../imagenes/sombrero.jpg')
alto_sombrero, ancho_sombrero, _ = sombrero.shape
talla_sombrero = 1.4
proporciones_sombrero = ancho_sombrero/alto_sombrero

area_min = 10000

clasificador = cv2.CascadeClassifier('../haarcascades/haarcascade_frontalface_default.xml')

camara = cv2.VideoCapture(0)
if not camara.isOpened():
    print("No es posible abrir la cámara")
    exit()

ancho_ventana = int(camara.get(cv2.CAP_PROP_FRAME_WIDTH))
alto_ventana = int(camara.get(cv2.CAP_PROP_FRAME_HEIGHT))

while True:
    ret, frame = camara.read()
    if not ret:
        print("No es posible obtener la imagen")
        break

    frame_byn = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    caras = clasificador.detectMultiScale(frame_byn)
    for (x_cara, y_cara, ancho_cara, alto_cara) in caras:
        if ancho_cara*alto_cara > area_min:
            ancho_sombrero = int(ancho_cara*talla_sombrero)
            alto_sombrero = int(ancho_sombrero/proporciones_sombrero)
            sombrero = cv2.resize(sombrero, (ancho_sombrero, alto_sombrero))
            y_sombrero = y_cara-alto_sombrero
            x_sombrero = int(x_cara+ancho_cara/2-ancho_sombrero/2)
            if x_sombrero >= 0 and y_sombrero>= 0 and x_sombrero+ancho_sombrero <= ancho_ventana and y_sombrero+alto_sombrero <= alto_ventana :
                roi = frame[y_sombrero:y_sombrero+alto_sombrero, x_sombrero:x_sombrero+ancho_sombrero]
                roi = cv2.bitwise_and(sombrero, roi)
                frame[y_sombrero:y_sombrero+alto_sombrero, x_sombrero:x_sombrero+ancho_sombrero] = roi
  
    cv2.imshow('webcam',frame)

    if cv2.waitKey(10) == ord('q'): break

camara.release()
cv2.destroyAllWindows()

