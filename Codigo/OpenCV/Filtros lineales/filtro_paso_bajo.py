import cv2
  
img = cv2.imread('../imagenes/Invalidos.jpg', 0)

img_suavizada = cv2.blur(img, (10, 10))
cv2.imshow('Imagen filtrada', img_suavizada)

cv2.imshow('Imagen original', img)

cv2.waitKey(0)
cv2.destroyAllWindows()



