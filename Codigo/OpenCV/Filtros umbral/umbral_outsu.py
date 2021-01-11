import cv2
  
img = cv2.imread('../imagenes/degradado.jpg', 0)

_, img_umbral = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('Imagen filtrada', img_umbral)

cv2.imshow('Imagen original', img)

cv2.waitKey(0)
cv2.destroyAllWindows()



