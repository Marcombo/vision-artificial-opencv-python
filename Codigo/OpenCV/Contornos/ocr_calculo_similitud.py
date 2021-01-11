import cv2


umbral = 150

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

similitud12 = cv2.matchShapes(contorno1, contorno2, cv2.CONTOURS_MATCH_I1, 0.0)
similitud13 = cv2.matchShapes(contorno1, contorno3, cv2.CONTOURS_MATCH_I1, 0.0)
similitud23 = cv2.matchShapes(contorno2, contorno3, cv2.CONTOURS_MATCH_I1, 0.0)

print("similitud entre el 1 y el 2: ", similitud12)
print("similitud entre el 1 y el 3: ", similitud13)
print("similitud entre el 2 y el 3: ", similitud23)


