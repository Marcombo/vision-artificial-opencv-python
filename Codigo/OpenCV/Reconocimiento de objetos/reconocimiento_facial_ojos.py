import cv2

color = (0, 255, 255)
grosor = 2

clasificador_caras = cv2.CascadeClassifier('../haarcascades/haarcascade_frontalface_default.xml')
clasificador_ojos = cv2.CascadeClassifier('../haarcascades/haarcascade_eye.xml')


img = cv2.imread('../imagenes/Einstein.jpg')
img_byn = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

caras = clasificador_caras.detectMultiScale(img_byn)
for (x, y, ancho, alto) in caras:
    cv2.rectangle(img,(x, y),(x + ancho, y + alto),color, grosor)
    cara = img_byn[y:y+alto, x:x+ancho]
    ojos = clasificador_ojos.detectMultiScale(cara)
    for (x1, y1, ancho1, alto1) in ojos:
        radio = int((ancho1 + alto1)/4)
        cv2.circle(img, (x1 + x + radio, y1 + y + radio), radio, color, grosor)
  
cv2.imshow('Einstein',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

