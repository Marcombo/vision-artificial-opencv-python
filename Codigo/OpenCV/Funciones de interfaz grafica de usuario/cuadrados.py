import cv2 
  
img = cv2.imread('../imagenes/cuadro.jpg', 1)

alto, ancho, canales = img.shape
color = (0, 0, 255)
grosor = 2
separación = 10
numero_cuadrados = 10

centro_x = int(ancho/2)
centro_y = int(alto/2)

for lado in range(0, 100, separación):
    x1 = centro_x - int(lado*ancho/200)
    x2 = centro_x + int(lado*ancho/200)
    y1 = centro_y - int(lado*alto/200)
    y2 = centro_y + int(lado*alto/200)
    cv2.rectangle(img, (x1, y1), (x2, y2),color, grosor)

cv2.imshow('cuadro', img)
