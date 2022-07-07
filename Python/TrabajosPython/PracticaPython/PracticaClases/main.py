from Triangulo import Triangulo
from Cuadrado import Cuadrado
from Circulo import Circulo

from Prisma import Prisma
from Cubo import Cubo
from Esfera import Esfera

triangulo = Triangulo(5, 5)
print("Triangulo")
print("Area: ", triangulo.__calcularArea__())
print("Perimetro: ", triangulo.__calcularPerimetro__())
print("\n")

cuadrado = Cuadrado(25)
print("Cuadrado")
print("Area: ", cuadrado.__calcularArea__())
print("Perimetro: ", cuadrado.__calcularPerimetro__())
print("\n")

circulo = Circulo(5)
print("Circulo")
print("Area: ", circulo.__calcularArea__())
print("Perimetro: ", circulo.__calcularPerimetro__())
print("\n")

prisma = Prisma(5, 5)
print("Prisma")
print("Area: ", prisma.__calcularArea__())
print("Volumen: ", prisma.__calcularVolumen__())
print("\n")

cubo = Cubo(5)
print("Cubo")
print("Area: ", cubo.__calcularArea__())
print("Volumen: ", cubo.__calcularVolumen__())
print("\n")

esfera = Esfera(5)
print("Esfera")
print("Area: ", esfera.__calcularArea__())
print("Volumen: ", esfera.__calcularVolumen__())
print("\n")