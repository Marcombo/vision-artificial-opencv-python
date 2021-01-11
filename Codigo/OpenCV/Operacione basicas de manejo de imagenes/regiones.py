import cv2

color = (0, 0, 255)
grosor = 2
ancho_min = 125

img = cv2.imread('../imagenes/cuadro.jpg', 1)
img_original = img.copy()

cv2.imshow('Cuadro', img)

def region(event,x,y,flags,param):
    global x1, y1, img
    
    if event == cv2.EVENT_LBUTTONDOWN:
        x1, y1 = x, y
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON :
        img = img_original.copy()
        cv2.rectangle(img, (x1, y1), (x, y), color, grosor)
    elif event == cv2.EVENT_LBUTTONUP :
        if x > x1 and y > y1 and x - x1 > ancho_min:
            img_recortada = img_original[y1:y, x1:x]
            cv2.imshow('Recorte',img_recortada)

    cv2.imshow('Cuadro',img)

cv2.setMouseCallback('Cuadro',region)

key = cv2.waitKey(0)
cv2.destroyAllWindows()
