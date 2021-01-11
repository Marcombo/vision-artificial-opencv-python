import cv2
  
img = cv2.imread('../imagenes/cuadro.jpg', 1)
img_original = img.copy()

color = (0, 0, 255)
grosor = 4
fuente = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
escala = 2
alto_imagen, ancho_imagen, canales = img.shape

def actualizar_imagen(escala):
    img = img_original.copy()
    posicion_x, posicion_y = centrarImagen(escala)
    cv2.putText(img, "Isabel", (posicion_x, posicion_y), fuente, escala, color, grosor)
    cv2.imshow('Cuadro', img)

def centrarImagen(escala):
    (ancho_texto, alto_texto), _ = cv2.getTextSize("Isabel", fuente, escala, grosor)
    posicion_x = int((ancho_imagen - ancho_texto) / 2)
    posicion_y = int((alto_imagen + alto_texto) / 2)
    return posicion_x, posicion_y

posicion_x, posicion_y = centrarImagen(escala)
cv2.putText(img, "Isabel", (posicion_x, posicion_y), fuente, escala, color, grosor)
cv2.imshow('Cuadro', img)
cv2.createTrackbar('Escala texto', 'Cuadro', 2, 5, actualizar_imagen)

