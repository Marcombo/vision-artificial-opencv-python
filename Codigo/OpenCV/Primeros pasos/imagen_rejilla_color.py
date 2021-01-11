import cv2
import numpy

ancho = alto = 300

img = numpy.ones((alto,ancho, 3),numpy.uint8)*255
img[:] = (255, 255, 255)

for x in range(ancho):
    for y in range(alto):
        if x%50 == 0 or  y%50 == 0:
            img[y, x] = (0, 0, 255)

cv2.imshow('Rejilla ', img)

