import cv2

carpeta_fotogramas = '../imagenes/secuencia_webcam'
numero_fotograma = 0
numero_fotogramas = 10
grabando = False

camara = cv2.VideoCapture(0)

if not camara.isOpened():
    print("No es posible abrir la cámara")
    exit()
while numero_fotograma < numero_fotogramas:
    ret, frame = camara.read()
    if not ret:
        print("No es posible obtener la imagen")
        break

    cv2.imshow('webcam', frame)
    
    if cv2.waitKey(100) == ord(' '):
        grabando = True
        print("Inicio grabacion")
    if grabando:
        print('Grabando '+'/fotograma'+str(numero_fotograma)+'.jpg')
        cv2.imwrite(carpeta_fotogramas+'/fotograma'+str(numero_fotograma)+'.jpg', frame)
        numero_fotograma +=1

print("Fin grabacion")
camara.release()
cv2.destroyAllWindows()
