import cv2

color = (0, 155, 255)
grosor = 2

img = cv2.imread('../imagenes/coliseo.jpg')
patron = cv2.imread('../imagenes/coliseo_recorte.jpg')

res = cv2.matchTemplate(img, patron, cv2.TM_SQDIFF_NORMED)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
esq_sup_izq = min_loc
alto, ancho, _ = patron.shape
esq_inf_der = (esq_sup_izq[0] + ancho, esq_sup_izq[1] + alto)

cv2.rectangle(img, esq_sup_izq, esq_inf_der, color, grosor)

cv2.imshow('Imagen original', img)
cv2.imshow('Patron', patron)


cv2.waitKey(0)
cv2.destroyAllWindows()
