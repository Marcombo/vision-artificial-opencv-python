import cv2

monoculo = cv2.imread('../imagenes/monoculo.jpg')
alto_monoculo, ancho_monoculo, _ = monoculo.shape
talla_monoculo = 1.3
offset_monoculo = 5

proporciones_monoculo = ancho_monoculo/alto_monoculo

clasificador = cv2.CascadeClassifier('../haarcascades/haarcascade_frontalface_default.xml')
clasificador_ojos = cv2.CascadeClassifier('../haarcascades/haarcascade_eye.xml')

img = cv2.imread('../imagenes/Einstein.jpg')
img_byn = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

alto_imagen, ancho_imagen, _ = img.shape

caras = clasificador.detectMultiScale(img_byn)
for (x_cara, y_cara, ancho_cara, alto_cara) in caras:
    cara = img_byn[y_cara:y_cara+alto_cara, x_cara:x_cara+ancho_cara]
    ojos = clasificador_ojos.detectMultiScale(cara)
    if len(ojos) != 2 : continue
    (x_ojo0, y_ojo0, ancho_ojo0, _) = ojos[0]
    (x_ojo1, y_ojo1, ancho_ojo1, _) = ojos[1]
    if x_ojo0 > x_ojo1 :
        x_ojo = x_ojo0 + int(ancho_ojo0/offset_monoculo)
        y_ojo = y_ojo0
        ancho_ojo = ancho_ojo0
    else:
        x_ojo = x_ojo1 + int(ancho_ojo1/offset_monoculo)
        y_ojo = y_ojo1
        ancho_ojo = ancho_ojo1

    ancho_monoculo = int(ancho_ojo*talla_monoculo)
    alto_monoculo = int(ancho_monoculo/proporciones_monoculo)
    monoculo = cv2.resize(monoculo, (ancho_monoculo, alto_monoculo))
    y_monoculo = y_ojo + y_cara
    x_monoculo = x_ojo + y_cara
    
    if x_monoculo >= 0 and y_monoculo >= 0 and x_monoculo+ancho_monoculo <= ancho_imagen and y_monoculo+alto_monoculo <= alto_imagen :
        roi = img[y_monoculo:y_monoculo+alto_monoculo, x_monoculo:x_monoculo+ancho_monoculo]
        roi = cv2.bitwise_and(monoculo, roi)
        img[y_monoculo:y_monoculo+alto_monoculo, x_monoculo:x_monoculo+ancho_monoculo] = roi
  
cv2.imshow('Einstein',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

