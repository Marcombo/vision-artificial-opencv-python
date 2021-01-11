import cv2

img = cv2.imread('../imagenes/cuadro.jpg')
img_original = img.copy()
cv2.imshow('Imagen', img)

def incrementa_brillo(brillo):
    img = img_original.copy()
    
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    limite = 255 - brillo
    v[v > limite] = 255
    v[v <= limite] += brillo

    hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    cv2.imshow('Imagen', img)

cv2.createTrackbar('Incremento', 'Imagen', 0, 255, incrementa_brillo)

cv2.waitKey(0)
cv2.destroyAllWindows()
