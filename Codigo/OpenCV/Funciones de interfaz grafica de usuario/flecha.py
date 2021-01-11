import cv2 
  
img = cv2.imread('../imagenes/cuadro.jpg', 1)

cv2.arrowedLine(img, (200, 100), (300, 150),(0, 0, 255), 5)

cv2.imshow('cuadro', img)
