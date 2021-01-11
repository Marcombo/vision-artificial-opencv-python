import cv2

archivo_persona = '../imagenes/Humphrey.jpg'
archivo_cara = '../imagenes/caras/Humphrey.jpg'

clasificador = cv2.CascadeClassifier('../haarcascades/haarcascade_frontalface_default.xml')

img = cv2.imread(archivo_persona)
img_byn = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

caras = clasificador.detectMultiScale(img_byn)
x, y, ancho, alto = caras[0]
img_cara = img[y:y+alto, x:x+ancho]
cv2.imwrite(archivo_cara, img_cara)
  
print("Cara almacenada")

