import cv2
import numpy as np

intervalo = 5

img = cv2.imread('../imagenes/lgtb.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

def filtra_matiz(matiz):
    matiz_inferior = np.array([matiz- intervalo,0,0])
    matiz_superior = np.array([matiz + intervalo,255,255])
    mascara = cv2.inRange(hsv, matiz_inferior, matiz_superior)

    res = cv2.bitwise_and(img,img, mask=mascara)

    cv2.imshow('Mascara',mascara)
    cv2.imshow('Imagen filtrada',res)
    cv2.imshow('Imagen original',img)

filtra_matiz(0)

cv2.createTrackbar('Matiz', 'Imagen original', 0, 179, filtra_matiz)

cv2.waitKey(0)
cv2.destroyAllWindows()



