import cv2 
  
img = cv2.imread('../imagenes/cuadro.jpg', 1)

alto, ancho, _ = img.shape
color = (0, 0, 255)
grosor = 2
cuadricula = 80

for x in range(0, ancho+1, cuadricula):
    img = cv2.line(img, (x, 0), (x, alto), color, grosor)
for y in range(0, alto+1, cuadricula):
    img = cv2.line(img, (0, y), (ancho, y), color, grosor)

cv2.imshow('cuadro', img)
