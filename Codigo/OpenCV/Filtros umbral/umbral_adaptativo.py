import cv2

bloque = 3
constante = 0

def actualizar_bloque(blq):
    global bloque
    bloque = blq
    if bloque < 3 : bloque = 3
    elif bloque%2 == 0 : bloque += 1
    img_umbral = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,bloque,constante)
    cv2.imshow('Imagen filtrada', img_umbral)

def actualizar_constante (cte):
    global constante
    constante = cte
    img_umbral = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,bloque,constante)
    cv2.imshow('Imagen filtrada', img_umbral)

img = cv2.imread('../imagenes/tabla_numeros.jpg', 0)

img_umbral = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,bloque,constante)
cv2.imshow('Imagen filtrada', img_umbral)

cv2.imshow('Imagen original', img)
cv2.createTrackbar('Bloque', 'Imagen original', bloque, 500, actualizar_bloque)
cv2.createTrackbar('Constante', 'Imagen original', constante, 255, actualizar_constante)

cv2.waitKey(0)
cv2.destroyAllWindows()




