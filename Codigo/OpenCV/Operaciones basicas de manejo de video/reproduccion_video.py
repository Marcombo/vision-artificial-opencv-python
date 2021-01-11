import cv2

fps = 30
velocidad_reproduccion = int(1000/fps) #milisegundos

#Se crea el objeto que representa la fuente de video
video = cv2.VideoCapture('../videos/video.avi')
#Si no se ha podido acceer a la fuente de video se sale del programa
if not video.isOpened():
    print("No es posible abrir el archivo")
    exit()
while True:
    # Se captura la imagen frame a frame
    ret, frame = video.read()
    # Cuando el video termina, se sale del bucle
    if not ret:
        print("Reproducción finalizada")
        break
    # El frame se muestra en pantalla
    cv2.imshow('video', frame)
    if cv2.waitKey(velocidad_reproduccion) == ord('q'):
        break
# Se libera la cámara y se cierra la ventana
video.release()
cv2.destroyAllWindows()
