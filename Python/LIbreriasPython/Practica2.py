import cv2 

import numpy as np

imagen1 = "D:/Users/EMI VOZ DE ESPERANZA/Desktop/TrabajosPython/Images/coins-400286_960_720.jpg"

imagen = cv2.imread(imagen1)

gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

valor1 = 3
valor2 = 6

gauss = cv2.GaussianBlur(gray, (valor1, valor1), 0)

canny = cv2.Canny(gauss,60,100)

kernel = np.ones((valor2, valor2), np.uint8)

cierre = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel)

contornos, jerarquia = cv2.findContours(cierre.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print ("Monedad encontrada: {}".format(len(contornos)))

cv2.drawContours(imagen, contornos, -1, (0,0,255), 2)

cv2.imshow("Salida", imagen)
cv2.imshow("EscalaGrises", gray)
cv2.imshow("PruebaEnfoque", gauss) 
cv2.imshow("PruebaGrises", canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
