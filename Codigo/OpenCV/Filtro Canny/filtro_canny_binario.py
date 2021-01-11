import cv2
  
img = cv2.imread('../imagenes/cuadro.jpg', 0)

img_canny = cv2.Canny(img, 100, 200)
_, img_inversa = cv2.threshold(img_canny, 0, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('Imagen filtrada', img_inversa)

cv2.waitKey(0)
cv2.destroyAllWindows()


