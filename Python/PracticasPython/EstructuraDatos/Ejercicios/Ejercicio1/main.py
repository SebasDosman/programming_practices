from menu import Menu
from pila import Pila, apilar, tamano, barrido, eliminar_elemento
from persona import Persona

pila = Pila()

Menu.opcionesMenu()
opcion = int(input("Digite una opcion \n"))

while(opcion != 4):    
    if (opcion == 1):
        nombre = input("Ingrese nombre de la persona \n")
        edad = int(input("Ingrese la edad de la persona \n"))
        
        persona = Persona(nombre, edad)
        apilar(pila, persona)
        
        Menu.opcionesMenu()
        opcion = int(input("Digite una opcion \n"))
    elif (opcion == 2):
        print("Cantidad de personas: ")
        print(tamano(pila))
        print("Personas dentro del bus: ")
        barrido(pila)
        
        Menu.opcionesMenu()
        opcion = int(input("Digite una opcion \n"))
    elif (opcion == 3):
        nombreBuscar = input("Ingrese nombre de la persona a buscar \n")
        eliminar_elemento(pila, nombreBuscar)
        
        Menu.opcionesMenu()
        opcion = int(input("Digite una opcion \n"))
    else:
        print("Digite una opcion correspondiente")
        
        Menu.opcionesMenu()
        opcion = int(input("Digite una opcion \n"))

print("Gracias por usar el programa")