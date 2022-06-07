import cv2

path = "D:/Users/EMI VOZ DE ESPERANZA/Desktop/TrabajosPython/Images/Imagen1.png"

imagen = cv2.imread(path)

gray = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)

tipoUmbral,umbral = cv2.threshold(gray,225,255,cv2.THRESH_BINARY)

contorno, jerarquia = cv2.findContours(umbral,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(imagen,contorno,-1,(0,255,0),4)

# cv2.imshow("EscalaGrises",gray)
# cv2.imshow("binario",umbral)
cv2.imshow("ImagenContorno",imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()