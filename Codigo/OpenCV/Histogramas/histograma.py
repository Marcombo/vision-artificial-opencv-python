import cv2
from matplotlib import pyplot as plt 

img = cv2.imread('../imagenes/Moises.jpg', 0)

hist = cv2.calcHist([img],[0],None,[256],[0,256]) 

print(hist)
cv2.imshow('Imagen', img)

plt.xlabel('Nivel de luz')
plt.ylabel('Nº de pixeles')
plt.title('Histograma')
plt.plot(hist)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
