import cv2

def actualizar_imagen(umbral):
    _, img_umbral = cv2.threshold(img, umbral, 255, cv2.THRESH_BINARY)
    cv2.imshow('Imagen filtrada', img_umbral)
  
img = cv2.imread('../imagenes/degradado.jpg', 0)

actualizar_imagen(0)

cv2.imshow('Imagen original', img)
cv2.createTrackbar('Umbral', 'Imagen original', 0, 255, actualizar_imagen)

cv2.waitKey(0)
cv2.destroyAllWindows()



