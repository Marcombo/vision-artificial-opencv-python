import cv2

#Se crea el objeto que representa la fuente de video
camara = cv2.VideoCapture(0)
#Si no se ha podido acceer a la fuente de video se sale del programa
if not camara.isOpened():
    print("No es posible abrir la cámara")
    exit()
while True:
    # Se captura la imagen frame a frame
    ret, frame = camara.read()
    # Si la captura no se ha tomado correctamente se sale del bucle
    if not ret:
        print("No es posible obtener la imagen")
        break
    # El frame se muestra en pantalla
    cv2.imshow('webcam', frame)
    if cv2.waitKey(1) == ord('q'):
        break
# Se libera la cámara y se cierra la ventana
camara.release()
cv2.destroyAllWindows()
