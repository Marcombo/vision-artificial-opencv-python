import cv2

fuente = cv2.FONT_HERSHEY_COMPLEX
color = (0,255,255)
grosor = 2
escala = 1
posicion_texto_1 = (20, 30)
posicion_texto_2 = (20, 60)
posicion_texto_5 = (20, 90)
(ancho_texto, alto_texto), _ = cv2.getTextSize(" ", fuente, escala, grosor)

umbral = 120

area_min_1 = 4000
area_min_2 = 6000
area_min_5 = 8000

area_max = 10000

num_monedas_1 = num_monedas_2 = num_monedas_5 = 0

incremento_brillo = 0

def modifica_brillo(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    limite = 255 - incremento_brillo
    v[v > limite] = 255
    v[v <= limite] += incremento_brillo

    hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    return img

def incrementa_brillo(valor):
    global incremento_brillo
    incremento_brillo = valor

cv2.namedWindow('webcam')
cv2.createTrackbar('Brillo', 'webcam', 0, 255, incrementa_brillo)

camara = cv2.VideoCapture(0)
if not camara.isOpened():
    print("No es posible abrir la cámara")
    exit()

while True:
    ret, frame = camara.read()
    if not ret:
        print("No es posible obtener la imagen")
        break

    frame = modifica_brillo(frame)

    frame_byn = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    frame_suavizado = cv2.blur(frame_byn, (10, 10))
    _, frame_umbral = cv2.threshold(frame_suavizado, umbral, 255, cv2.THRESH_BINARY_INV)
    contornos, _ = cv2.findContours(frame_umbral, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    #cv2.drawContours(frame, contornos, -1, color, grosor)
    
    num_monedas_1 = num_monedas_2 = num_monedas_5 = 0
    for contorno in contornos:
        area = abs(cv2.contourArea(contorno, True))
        #print(area)
        (x, y), _ = cv2.minEnclosingCircle(contorno)
        centro_objeto = (int(x-ancho_texto/2), int(y+alto_texto/2))
        if area <= area_max:
            if area >= area_min_5:
                num_monedas_5 += 1
                cv2.putText(frame, "5", centro_objeto, fuente, escala, color, grosor)
            elif area >= area_min_2:
                num_monedas_2 += 1
                cv2.putText(frame, "2", centro_objeto, fuente, escala, color, grosor)
            elif area >= area_min_1:
                num_monedas_1 += 1
                cv2.putText(frame, "1", centro_objeto, fuente, escala, color, grosor)

    cv2.putText(frame, "Monedas de 1 centimo:  " + str(num_monedas_1), posicion_texto_1, fuente, escala, color, grosor)
    cv2.putText(frame, "Monedas de 2 centimos: " + str(num_monedas_2), posicion_texto_2, fuente, escala, color, grosor)
    cv2.putText(frame, "Monedas de 5 centimos: " + str(num_monedas_5), posicion_texto_5, fuente, escala, color, grosor)

    cv2.imshow('webcam', frame)
    
    if cv2.waitKey(1) == ord('q'): break

camara.release()
cv2.destroyAllWindows()




