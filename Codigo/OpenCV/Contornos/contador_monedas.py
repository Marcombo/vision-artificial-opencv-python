import cv2

fuente = cv2.FONT_HERSHEY_COMPLEX
color = (0,255,255)
grosor = 2
escala = 1
posicion_texto_1 = (20, 30)
posicion_texto_2 = (20, 60)
posicion_texto_5 = (20, 90)

umbral = 120

area_min_1 = 4000
area_min_2 = 6000
area_min_5 = 8000

num_monedas_1 = num_monedas_2 = num_monedas_5 = 0

img = cv2.imread('../imagenes/monedas2.jpg')
img_byn = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, img_umbral = cv2.threshold(img_byn, umbral, 255, cv2.THRESH_BINARY_INV)
contornos, _ = cv2.findContours(img_umbral, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
#cv2.drawContours(img, contornos, -1, color, grosor)

for contorno in contornos:
    area = abs(cv2.contourArea(contorno, True))
    if area >= area_min_5: num_monedas_5 += 1
    elif area >= area_min_2: num_monedas_2 += 1
    elif area >= area_min_1: num_monedas_1 += 1

cv2.putText(img, "Monedas de 1 centimo:  " + str(num_monedas_1), posicion_texto_1, fuente, escala, color, grosor)
cv2.putText(img, "Monedas de 2 centimos: " + str(num_monedas_2), posicion_texto_2, fuente, escala, color, grosor)
cv2.putText(img, "Monedas de 5 centimos: " + str(num_monedas_5), posicion_texto_5, fuente, escala, color, grosor)
cv2.imshow('Contornos', img)

cv2.waitKey(0)
cv2.destroyAllWindows()




