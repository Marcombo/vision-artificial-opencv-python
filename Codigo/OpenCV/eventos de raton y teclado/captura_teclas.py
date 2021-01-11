import cv2
import numpy

img = numpy.ones((300,300),numpy.uint8)*255
cv2.imshow('Captura teclas', img)

while True:
    key = cv2.waitKey(100)
    if key != -1:
        print(key)
