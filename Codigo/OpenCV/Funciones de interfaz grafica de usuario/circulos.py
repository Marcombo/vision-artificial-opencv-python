import cv2 
  
img = cv2.imread('../imagenes/cuadro.jpg', 1)

alto, ancho, canales = img.shape
color = (0, 0, 255)
incremento_radio = 80
grosor = 40

centro_x = int(ancho/2)
centro_y = int(alto/2)

for radio in range(0, int(alto/2)+1, incremento_radio):
    cv2.circle(img, (centro_x, centro_y), radio,color, grosor)

cv2.imshow('cuadro', img)
