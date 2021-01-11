import cv2 
  
img1 = cv2.imread('../imagenes/wikipedia0.jpg', 0)
img2 = cv2.imread('../imagenes/wikipedia3.jpg', 0)

img = cv2.subtract(img1, img2)

cv2.imshow('Sustraccion imagenes', img)
