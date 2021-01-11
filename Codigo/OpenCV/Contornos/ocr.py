import cv2


umbral = 150

similitud = 0.1

fuente = cv2.FONT_HERSHEY_SIMPLEX
color = 0
grosor = 2
escala = 1
posicion = (20, 30)
numeros = "Numeros: "

img = cv2.imread('../imagenes/numeros.jpg', 0)

img1 = cv2.imread('../imagenes/uno.jpg',0)
img2 = cv2.imread('../imagenes/dos.jpg',0)
img3 = cv2.imread('../imagenes/tres.jpg',0)

_, img1_umbral = cv2.threshold(img1, umbral, 255, cv2.THRESH_BINARY_INV)
_, img2_umbral = cv2.threshold(img2, umbral, 255, cv2.THRESH_BINARY_INV)
_, img3_umbral = cv2.threshold(img3, umbral, 255, cv2.THRESH_BINARY_INV)
contornos1, _ = cv2.findContours(img1_umbral, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
contornos2, _ = cv2.findContours(img2_umbral, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
contornos3, _ = cv2.findContours(img3_umbral, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
contorno1 = contornos1[0]
contorno2 = contornos2[0]
contorno3 = contornos3[0]

_, img_umbral = cv2.threshold(img, umbral, 255, cv2.THRESH_BINARY_INV)
contornos, _ = cv2.findContours(img_umbral, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
for contorno in contornos:
    if cv2.matchShapes(contorno,contorno1,cv2.CONTOURS_MATCH_I1,0.0) <= similitud:
        numeros = numeros + "1"
    elif cv2.matchShapes(contorno,contorno2,cv2.CONTOURS_MATCH_I1,0.0) <= similitud:
        numeros = numeros + "2"
    elif cv2.matchShapes(contorno,contorno3,cv2.CONTOURS_MATCH_I1,0.0) <= similitud:
        numeros = numeros + "3"

cv2.putText(img, numeros, posicion, fuente, escala, color, grosor)
cv2.imshow('Numeros', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
