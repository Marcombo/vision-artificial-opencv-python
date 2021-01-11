import cv2 
  
img1 = cv2.imread('../imagenes/espacio.jpg', 1)
img2 = cv2.imread('../imagenes/tierra.jpg', 1)

img = cv2.addWeighted(img1, 0.4, img2, 0.8, 0)

cv2.imshow('Composicion imagenes', img)
