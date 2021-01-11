import cv2
import numpy as np

kernel = np.ones((2,2),np.uint8)
  
img = cv2.imread('../imagenes/Invalidos_ruido.jpg', 0)

img_dilatada = cv2.dilate(img,kernel)

cv2.imshow('Imagen filtrada', img_dilatada)

cv2.imshow('Imagen original', img)

cv2.waitKey(0)
cv2.destroyAllWindows()



