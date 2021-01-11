import numpy as np
import cv2

objeto_seleccionado = False

ancho = 100
alto = 100
color = (0, 255, 255)
grosor = 2

criterios_parada = (cv2.TERM_CRITERIA_COUNT | cv2.TERM_CRITERIA_EPS, 15, 2)

def eventos_raton(evento, x, y, flags, parametros):
    global roi_hist, ventana_seguimiento, objeto_seleccionado

    if evento == cv2.EVENT_LBUTTONDOWN:
        objeto_seleccionado = True
        x = int(x-ancho/2)
        y = int(y-alto/2)
        ventana_seguimiento = (x, y, ancho, alto)
        roi = frame[y:y+alto, x:x+ancho]
        hsv_roi =  cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
        mascara = cv2.inRange(hsv_roi, np.array((0,60,32)), np.array((180,255,255)))
        roi_hist = cv2.calcHist([hsv_roi],[0],mascara,[180],[0,180])
        cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)
        

camara = cv2.VideoCapture(0)
if not camara.isOpened():
    print("No es posible abrir la cámara")
    exit()
    
cv2.namedWindow('webcam')
cv2.setMouseCallback('webcam', eventos_raton)

while(True):
    ret, frame = camara.read()
    if not ret:
        print("No es posible obtener la imagen")
        break
    if objeto_seleccionado:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)
        cv2.imshow('retroproyeccion',dst)
        _, ventana_seguimiento = cv2.meanShift(dst, ventana_seguimiento, criterios_parada)
        x,y,ancho,alto = ventana_seguimiento
        frame = cv2.rectangle(frame, (x,y), (x+ancho,y+alto), color, grosor)

    cv2.imshow('webcam',frame)

    if cv2.waitKey(1) == ord('q'): break
    
camara.release()
cv2.destroyAllWindows()
