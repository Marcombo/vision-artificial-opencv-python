import cv2
import numpy

ancho = alto = 300

img = numpy.ones((alto,ancho),numpy.uint8)*255

for x in range(ancho):
    for y in range(alto):
        if x%50 == 0 or  y%50 == 0:
            img[y, x] = 0

cv2.imwrite('../imagenes/rejilla.jpg', img)
print("Imagen almacenada")

