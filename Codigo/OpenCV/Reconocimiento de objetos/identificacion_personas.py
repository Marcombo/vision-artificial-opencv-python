import cv2
from os import listdir

color = (0, 255, 255)
grosor = 2
fuente = cv2.FONT_HERSHEY_COMPLEX
escala = 1

carpeta_caras = '../imagenes/caras/'
lista_nombres = []
lista_caras = []

error = 10

for archivo in listdir(carpeta_caras):
    lista_nombres.append(archivo.replace(".jpg",""))
    lista_caras.append(cv2.imread(carpeta_caras+archivo, 0))

clasificador = cv2.CascadeClassifier('../haarcascades/haarcascade_frontalface_default.xml')

img = cv2.imread('../imagenes/Humphrey_Ingrid.jpg')
img_byn = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

caras = clasificador.detectMultiScale(img_byn)
for (x, y, ancho, alto) in caras:
    #cv2.rectangle(img,(x, y),(x + ancho, y + alto),color, grosor)
    for indice in range(len(lista_caras)):
        patron = cv2.resize(lista_caras[indice], (ancho, alto))
        res = cv2.matchTemplate(img_byn, patron, cv2.TM_SQDIFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        esq_sup_izq = min_loc

        (x1, y1) = esq_sup_izq
        if abs(x-x1) < error and abs(y-y1) < error :
            #esq_inf_der_ingrid = (esq_sup_izq_ingrid[0] + ancho, esq_sup_izq_ingrid[1] + alto)
            #cv2.rectangle(img, esq_sup_izq_ingrid, esq_inf_der_ingrid, (0, 0, 255), grosor)
            cv2.putText(img, lista_nombres[indice], (x, y), fuente, escala, color, grosor)
            break
    
cv2.imshow('Identificacion personas',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

