import cv2

color = (0, 255, 255)
grosor = 2

clasificador = cv2.CascadeClassifier('../haarcascades/haarcascade_frontalface_default.xml')

img = cv2.imread('../imagenes/Tesla.jpg')
img_byn = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

caras = clasificador.detectMultiScale(img_byn)
for (x, y, ancho, alto) in caras:
    cv2.rectangle(img,(x, y),(x + ancho, y + alto),color, grosor)
  
cv2.imshow('Tesla',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

