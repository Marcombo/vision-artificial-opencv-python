import cv2

umbral = 25

color = (0,255,255)
grosor = 3
tamanio_flecha = 50

  
img1 = cv2.imread('../imagenes/mercado1.jpg')
img2 = cv2.imread('../imagenes/mercado2.jpg')

img = cv2.subtract(img1, img2)
img_byn = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_suavizada = cv2.blur(img_byn, (10, 10))
_, img_umbral = cv2.threshold(img_suavizada, umbral, 255, cv2.THRESH_BINARY)
contornos, _ = cv2.findContours(img_umbral, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

for contorno in contornos:
    x,y,ancho,alto = cv2.boundingRect(contorno)
    x_extremo1 = x + ancho + tamanio_flecha
    y_extremo1 = y + int(alto/2) - tamanio_flecha
    x_extremo2 = x + ancho
    y_extremo2 = y + int(alto/2)
    cv2.arrowedLine(img1, (x_extremo1, y_extremo1), (x_extremo2, y_extremo2), color, grosor)

#cv2.drawContours(img1, contornos, -1, color, grosor)
#cv2.imshow('Imagen binarizada', img_umbral)
cv2.imshow('Imagen 1', img1)
cv2.imshow('Imagen 2', img2)


cv2.waitKey(0)
cv2.destroyAllWindows()
