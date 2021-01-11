import cv2

color = (0, 255, 255)
grosor = 2
area_min = 50000

carpeta_fotogramas = '../imagenes/alarma'

backSub = cv2.createBackgroundSubtractorKNN()

camara = cv2.VideoCapture(0)
if not camara.isOpened():
    print("No es posible abrir la cámara")
    exit()

while(True):
    ret, frame = camara.read()
    if not ret:
        print("No es posible obtener la imagen")
        break
    mascara_1er_plano = backSub.apply(frame)
    contornos, _ = cv2.findContours(mascara_1er_plano, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    if len(contornos):
        contorno_max = max(contornos, key = cv2.contourArea)
        area = abs(cv2.contourArea(contorno_max, True))
        #print(area)
        if area > area_min:
            cv2.imwrite(carpeta_fotogramas+'/fotograma.jpg', frame)

    cv2.drawContours(frame, [contorno_max], 0, color, grosor)
    cv2.imshow('webcam',frame)
    cv2.imshow('mascara 1er plano',mascara_1er_plano)

    if cv2.waitKey(1) == ord('q'): break
    
camara.release()
cv2.destroyAllWindows()
