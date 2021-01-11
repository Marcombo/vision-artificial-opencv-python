import cv2

umbral = 175
color = (0,0,255)
grosor = 3
  
img = cv2.imread('../imagenes/hoja.jpg')

img_byn = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, img_umbral = cv2.threshold(img_byn, umbral, 255, cv2.THRESH_BINARY_INV)
contornos, _ = cv2.findContours(img_umbral, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

for contorno in contornos:
    x,y,ancho,alto = cv2.boundingRect(contorno)
    cv2.rectangle(img,(x,y),(x+ancho,y+alto), color, grosor)

#cv2.drawContours(img, contornos, -1, color, grosor)
cv2.imshow('Bounding box', img)

cv2.waitKey(0)
cv2.destroyAllWindows()




