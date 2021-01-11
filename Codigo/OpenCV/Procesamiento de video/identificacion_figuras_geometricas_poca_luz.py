import cv2

umbral = 200

fuente = cv2.FONT_HERSHEY_SIMPLEX
color = (0,0,0)
grosor = 2
escala = 1
texto = ""

area_min = 10000

area_max = 50000

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
    global frame
    ret, frame = camara.read()
    if not ret:
        print("No es posible obtener la imagen")
        break

    frame = modifica_brillo(frame)

    frame_byn = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_suavizado = cv2.blur(frame_byn, (10, 10))
    _, frame_umbral = cv2.threshold(frame_suavizado, umbral, 255, cv2.THRESH_BINARY_INV)

    contornos, _ = cv2.findContours(frame_umbral, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    for contorno in contornos:
        x,y,ancho,alto = cv2.boundingRect(contorno)

        margen_error = 0.05*cv2.arcLength(contorno, True )
        contorno_aprox = cv2.approxPolyDP(contorno, margen_error, True )
        area = abs(cv2.contourArea(contorno_aprox, True))
        if area >= area_min and area < area_max:
            cv2.drawContours(frame, [contorno_aprox], 0, color, grosor)
            
            if len(contorno_aprox) == 3: texto = "TRIANGULO"  
            elif len(contorno_aprox) == 4:texto = "CUADRADO"
            elif len(contorno_aprox) == 5: texto = "PENTAGONO"

            (ancho_texto, alto_texto), _ = cv2.getTextSize(texto, fuente, escala, grosor)
            posicion_x = int(x + (ancho - ancho_texto) / 2)
            posicion_y = int(y + (alto / 2 + alto_texto / 2))

            cv2.putText(frame, texto, (posicion_x, posicion_y), fuente, escala, color, grosor)

    cv2.imshow('webcam', frame)
    
    if cv2.waitKey(1) == ord('q'): break

camara.release()
cv2.destroyAllWindows()




