import cv2
import numpy

ancho = alto = 300

img = numpy.ones((alto,ancho),numpy.uint8)*255

cv2.imshow('Imagen blanca', img)

