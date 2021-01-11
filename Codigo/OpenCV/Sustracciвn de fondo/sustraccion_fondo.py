import cv2

backSub = cv2.createBackgroundSubtractorKNN()

camara = cv2.VideoCapture(0)
if not camara.isOpened():
    print("No es posible abrir la cámara")
    exit()

while(True):
    ret, frame = camara.read()
    if not ret:
        print("No es posible obtener la imagen")
        break
    mascara_1er_plano = backSub.apply(frame)

    cv2.imshow('webcam',frame)
    cv2.imshow('mascara 1er plano',mascara_1er_plano)

    if cv2.waitKey(1) == ord('q'): break
    
camara.release()
cv2.destroyAllWindows()
