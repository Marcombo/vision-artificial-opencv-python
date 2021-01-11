import cv2 
  
img = cv2.imread('../imagenes/cuadro.jpg', 1)
cv2.imshow('Cuadro', img)

tamanio = img.size
alto, ancho, canales = img.shape
tipo = img.dtype
print("Tamaño: " + str(tamanio) + " bytes")
print("Ancho: " + str(ancho) + " píxeles")
print("Alto: " + str(alto) + " píxeles")
print("Nº canales: " + str(canales))
print("Tipo: " + str(tipo))

