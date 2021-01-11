import cv2
import numpy as np

kernel = np.ones((10,10),np.uint8)

umbral = 175
color = (0,0,255)
grosor = 3
  
img = cv2.imread('../imagenes/hoja.jpg')

img_byn = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_erosionada = cv2.erode(img_byn,kernel)
_, img_umbral = cv2.threshold(img_erosionada, umbral, 255, cv2.THRESH_BINARY_INV)
contornos, _ = cv2.findContours(img_umbral, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

for contorno in contornos:
    (x, y), radio = cv2.minEnclosingCircle(contorno)
    centro = (int (x), int (y))
    radio = int (radio)
    cv2.circle (img, centro, radio, color, grosor)

cv2.imshow('Bounding box', img)

cv2.waitKey(0)
cv2.destroyAllWindows()




