import cv2

color = (0,255,255)
grosor = 3

img = cv2.imread('../imagenes/hoja.jpg')
img_original = img.copy()
img_byn = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def mostrar_imagen_binarizada(umbral):
    global img_umbral
    _, img_umbral = cv2.threshold(img_byn, umbral, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow('Imagen binarizada', img_umbral)

def mostrar_contornos():
    contornos, _ = cv2.findContours(img_umbral, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    img = img_original.copy()
    cv2.drawContours(img, contornos, -1, color, grosor)
    cv2.imshow('Contornos', img)

def actualizar_imagenes(umbral):
    mostrar_imagen_binarizada(umbral)
    mostrar_contornos()
  
actualizar_imagenes(0)

cv2.createTrackbar('Umbral', 'Contornos', 0, 255, actualizar_imagenes)

cv2.waitKey(0)
cv2.destroyAllWindows()




