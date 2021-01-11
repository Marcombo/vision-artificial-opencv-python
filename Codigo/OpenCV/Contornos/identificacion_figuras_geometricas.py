import cv2

umbral = 200

porcentaje_error = 0.01

fuente = cv2.FONT_HERSHEY_SIMPLEX
color = (0,0,0)
grosor = 2
escala = 1
texto = ""
  
img = cv2.imread('../imagenes/figuras_geometricas4.jpg')

img_byn = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, img_umbral = cv2.threshold(img_byn, umbral, 255, cv2.THRESH_BINARY_INV)

contornos, _ = cv2.findContours(img_umbral, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

for contorno in contornos:
    x,y,ancho,alto = cv2.boundingRect(contorno)

    margen_error = porcentaje_error*cv2.arcLength(contorno, True )
    contorno_aprox = cv2.approxPolyDP(contorno, margen_error, True )
    #cv2.drawContours(img, [contorno_aprox], 0, color, grosor)
    
    if len(contorno_aprox) == 3: texto = "TRIANGULO"  
    elif len(contorno_aprox) == 4:texto = "CUADRADO"
    elif len(contorno_aprox) == 5: texto = "PENTAGONO"

    (ancho_texto, alto_texto), _ = cv2.getTextSize(texto, fuente, escala, grosor)
    posicion_x = int(x + (ancho - ancho_texto) / 2)
    posicion_y = int(y + (alto / 2 + alto_texto / 2))

    cv2.putText(img, texto, (posicion_x, posicion_y), fuente, escala, color, grosor)

cv2.imshow('Figuras geometricas', img)

cv2.waitKey(0)
cv2.destroyAllWindows()




