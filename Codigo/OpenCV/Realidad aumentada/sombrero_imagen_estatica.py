import cv2

sombrero = cv2.imread('../imagenes/sombrero.jpg')
alto_sombrero, ancho_sombrero, _ = sombrero.shape
talla_sombrero = 1.4
proporciones_sombrero = ancho_sombrero/alto_sombrero


clasificador = cv2.CascadeClassifier('../haarcascades/haarcascade_frontalface_default.xml')

img = cv2.imread('../imagenes/Einstein.jpg')
img_byn = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

alto_imagen, ancho_imagen, _ = img.shape

caras = clasificador.detectMultiScale(img_byn)
for (x_cara, y_cara, ancho_cara, alto_cara) in caras:
    ancho_sombrero = int(ancho_cara*talla_sombrero)
    alto_sombrero = int(ancho_sombrero/proporciones_sombrero)
    sombrero = cv2.resize(sombrero, (ancho_sombrero, alto_sombrero))
    y_sombrero = y_cara-alto_sombrero
    x_sombrero = int(x_cara+ancho_cara/2-ancho_sombrero/2)
    
    if x_sombrero >= 0 and y_sombrero>= 0 and x_sombrero+ancho_sombrero <= ancho_imagen and y_sombrero+alto_sombrero <= alto_imagen :
        roi = img[y_sombrero:y_sombrero+alto_sombrero, x_sombrero:x_sombrero+ancho_sombrero]
        roi = cv2.bitwise_and(sombrero, roi)
        img[y_sombrero:y_sombrero+alto_sombrero, x_sombrero:x_sombrero+ancho_sombrero] = roi
  
cv2.imshow('Einstein',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

