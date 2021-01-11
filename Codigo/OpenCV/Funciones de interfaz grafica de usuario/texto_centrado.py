import cv2 
  
img = cv2.imread('../imagenes/cuadro.jpg', 1)

color = (0, 0, 255)
grosor = 4
fuente = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
escala = 2

(ancho_texto, alto_texto), _ = cv2.getTextSize("Isabel", fuente, escala, grosor)
alto_imagen, ancho_imagen, canales = img.shape

posicion_x = int((ancho_imagen - ancho_texto) / 2)
posicion_y = int(alto_imagen / 2 + alto_texto / 2)

cv2.putText(img, "Isabel", (posicion_x, posicion_y), fuente, escala, color, grosor)

cv2.imshow('cuadro', img)

