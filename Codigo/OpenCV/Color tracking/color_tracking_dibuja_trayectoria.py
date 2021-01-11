import cv2
import numpy as np

matiz_objetivo = 0
rango = 5

color = (0, 255, 255)
grosor = 4

lista_puntos = []
tamanio_lista = 50
dibujar = False

def selecciona_color(evento, x, y, flags, frame):
    global matiz_objetivo, lista_puntos, dibujar

    if evento == cv2.EVENT_LBUTTONDOWN:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)
        matiz_objetivo = h[y, x]

        dibujar = True
        lista_puntos = []
        
def selecciona_rango(valor):
    global rango
    rango = valor

def filtra_matiz(frame):
    frame_suavizado = cv2.blur(frame, (10, 10))
    hsv = cv2.cvtColor(frame_suavizado, cv2.COLOR_BGR2HSV)
    color_inferior = np.array([matiz_objetivo - rango,150,0])
    color_superior = np.array([matiz_objetivo + rango,255,255])
    mascara = cv2.inRange(hsv, color_inferior, color_superior)

    #mascara = cv2.dilate(mascara, None, iterations=4)
    #mascara = cv2.erode(mascara, None, iterations=2)

    res = cv2.bitwise_and(frame,frame, mask=mascara)

    contornos, _ = cv2.findContours(mascara, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

    #cv2.imshow('Mascara',mascara)
    #cv2.imshow('Imagen filtrada',res)

    return contornos

cv2.namedWindow('webcam')
cv2.createTrackbar('Rango', 'webcam', 5, 30, selecciona_rango)

camara = cv2.VideoCapture(0)
if not camara.isOpened():
    print("No es posible abrir la cámara")
    exit()

while True:
    ret, frame = camara.read()
    if not ret:
        print("No es posible obtener la imagen")
        break

    contornos = filtra_matiz(frame)
    if len(contornos) > 0 and dibujar:
        contorno_max = max(contornos, key = cv2.contourArea)
        (x, y), radio = cv2.minEnclosingCircle(contorno_max)
        x = int(x)
        y = int(y)
        if len(lista_puntos) >= tamanio_lista : lista_puntos. pop(0)
        lista_puntos.append((x, y))
        if len(lista_puntos) >= 2:
            punto_prev = lista_puntos[0]
            for punto in lista_puntos:
                cv2.line(frame, punto, punto_prev, color, grosor)
                punto_prev = punto

    frame = cv2.flip(frame, 1)
    cv2.imshow('webcam', frame)
    cv2.setMouseCallback('webcam', selecciona_color, frame)
    
    if cv2.waitKey(10) == ord('q'): break

camara.release()
cv2.destroyAllWindows()
