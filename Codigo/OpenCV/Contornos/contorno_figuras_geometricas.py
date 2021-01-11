import cv2

umbral = 200
color = (0,255,255)
grosor = 3
  
img = cv2.imread('../imagenes/figuras_geometricas3.jpg')

img_byn = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, img_umbral = cv2.threshold(img_byn, umbral, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('Imagen binarizada', img_umbral)

contornos, _ = cv2.findContours(img_umbral, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(img, contornos, -1, color, grosor)
cv2.imshow('Contorno', img)

cv2.waitKey(0)
cv2.destroyAllWindows()




