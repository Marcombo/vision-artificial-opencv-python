import cv2

color = (0, 255, 255)
grosor = 2

clasificador = cv2.CascadeClassifier('../haarcascades/haarcascade_frontalface_default.xml')

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

    caras = clasificador.detectMultiScale(frame_byn)
    for (x, y, ancho, alto) in caras:
        cv2.rectangle(frame,(x, y),(x + ancho, y + alto),color, grosor)

    cv2.imshow('webcam', frame)
    
    if cv2.waitKey(1) == ord('q'): break

camara.release()
cv2.destroyAllWindows()

