import cv2 
  
img1 = cv2.imread('../imagenes/cuadro.jpg', 1)
img2 = cv2.imread('../imagenes/logo.jpg', 1)

alto, ancho, _ = img2.shape
roi = img1[0:alto, 0:ancho]

roi = cv2.bitwise_and(img2, roi)
img1[0:alto, 0:ancho ] = roi

cv2.imshow('Composicion imagenes', img1)
