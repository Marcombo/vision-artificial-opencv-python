import cv2
  
img = cv2.imread('../imagenes/figuras_geometricas2.jpg', 0)

img_canny = cv2.Canny(img, 100, 200)
cv2.imshow('Imagen filtrada', img_canny)

cv2.imshow('Imagen original', img)

cv2.waitKey(0)
cv2.destroyAllWindows()


