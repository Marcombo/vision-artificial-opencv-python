import cv2

archivo_video = '../videos/video.avi'

#Se crea el objeto que representa la fuente de video
camara = cv2.VideoCapture(0)
# Se obtiene el código FourCC del codec DIVX
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
#Se crea el objeto VideoWriter 
video = cv2.VideoWriter(archivo_video, fourcc, 20, (640,  480))
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
    #El frame se guarda en el archivo
    video.write(frame)
    # El frame se muestra en pantalla
    cv2.imshow('webcam', frame)
    if cv2.waitKey(1) == ord('q'):
        break
# Se liberan los recursos utilizados y se cierra la ventana
camara.release()
video.release()
cv2.destroyAllWindows()
