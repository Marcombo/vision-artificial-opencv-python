import cv2 
  
img = cv2.imread('../imagenes/cuadro.jpg', 1)

color = (0, 0, 255)
grosor = 2
cara_x1, cara_x2 = 300, 550
cara_y1, cara_y2 = 20, 220

cv2.rectangle(img, (cara_x1, cara_y1), (cara_x2, cara_y2),color, grosor)

cv2.imshow('cuadro', img)

