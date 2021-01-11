import cv2
  
img = cv2.imread('../imagenes/Invalidos.jpg', 0)

img_paso_bajo = cv2.blur(img, (10, 10))
img_paso_alto = cv2.subtract(img, img_paso_bajo)
cv2.imshow('Imagen filtrada', img_paso_alto)

cv2.imshow('Imagen original', img)

cv2.waitKey(0)
cv2.destroyAllWindows()



