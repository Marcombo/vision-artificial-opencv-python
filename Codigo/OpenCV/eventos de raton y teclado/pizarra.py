import numpy
import cv2

color = (0, 0, 255)
grosor = 2

img = numpy.zeros((600, 600, 3), numpy.uint8)
img[:] = (255, 255, 255)
cv2.imshow('Pizarra',img)

def pinta(event,x,y,flags,param):
    global x_prev,y_prev
    if event == cv2.EVENT_LBUTTONDOWN:
        x_prev,y_prev = x,y
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        cv2.line(img,(x_prev,y_prev),(x,y),color, grosor)
        x_prev,y_prev = x,y

    cv2.imshow('Pizarra',img)

cv2.setMouseCallback('Pizarra',pinta)


