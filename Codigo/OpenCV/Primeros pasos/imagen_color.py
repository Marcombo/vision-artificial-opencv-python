import cv2
import numpy

ancho = alto = 300

img = numpy.ones((alto,ancho, 3),numpy.uint8)*255
img[:] = (255, 0, 0)

cv2.imshow('Imagen color', img)
