#Figuras 2D
from Triangulo import Triangulo
from Cuadrado import Cuadrado
from Circulo import Circulo

#Figuras 3D
from Prisma import Prisma
from Cubo import Cubo
from Esfera import Esfera

#Objetos
triangulo = Triangulo(5, 5)
print("Triangulo")
triangulo.__calcularArea__()
triangulo.__calcularPerimetro__()
print("\n")

cuadrado = Cuadrado(25)
print("Cuadrado")
cuadrado.__calcularArea__()
cuadrado.__calcularPerimetro__()
print("\n")

circulo1 = Circulo(5)
print("Circulo")
circulo.__calcularArea__()
circulo.__set_vertices__(5)
circulo.__calcularPerimetro__()
print("\n")

prisma = Prisma(5, 5)
print("Prisma")
prisma.__calcularArea__()
prisma.__calcularVolumen__()
print("\n")

cubo = Cubo(5)
print("Cubo")
cubo.__calcularArea__()
cubo.__calcularVolumen__()
print("\n")

esfera = Esfera(5)
print("Esfera")
esfera.__calcularArea__()
esfera.__calcularVolumen__()
print("\n")

#Diccionario de objetos
figurasGeometricas = {
    "Triangulo": triangulo, 
    "Cuadrado": cuadrado, 
    "Circulo": circulo, 
    "Prisma": prisma,
    "Cubo": cubo, 
    "Esfera": esfera
}

#Lista de objetos
figurasGeometricasArray = []
figurasGeometricasArray.append(triangulo)
figurasGeometricasArray.append(cuadrado)
figurasGeometricasArray.append(circulo)
figurasGeometricasArray.append(prisma)
figurasGeometricasArray.append(cubo)
figurasGeometricasArray.append(esfera)

print(figurasGeometricas)
print("\n")

print(figurasGeometricasArray)
print("\n")

print(type(triangulo))