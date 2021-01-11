import cv2
import numpy

ancho = alto = 300

img = numpy.zeros((alto,ancho),numpy.uint8)

cv2.imshow('Imagen negra', img)
