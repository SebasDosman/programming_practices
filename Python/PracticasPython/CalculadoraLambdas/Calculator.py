import math

# <-- Paradigma programación Funcional -->
def __pedirDato__():
    num = int(input("\nDigite el número \n"))
    return num

def __menu__():
    print("Menú: \n" + 
        "1. Suma \n" + 
        "2. Resta \n" + 
        "3. Multiplicacion \n" + 
        "4. División \n" + 
        "5. Potencia \n" + 
        "6. Raíz \n")

suma = lambda num1, num2 : num1 + num2
resta = lambda num1, num2 : num1 - num2
multiplicacion = lambda num1, num2 : num1 * num2
division = lambda num1, num2 : num1 / num2
potencia = lambda num1, num2 : math.pow(num1, num2)
raiz = lambda num1, num2 : math.pow(num1, 1 / num2)

def __main__():
    __menu__()
    opcion = int(input("Digite una de las opciones \n"))

    num1 = __pedirDato__()
    num2 = __pedirDato__()
    
    if (opcion == 1):
        print("\n", int(suma(num1, num2)))
    elif (opcion == 2):
        print("\n", int(resta(num1, num2)))
    elif (opcion == 3):
        print("\n", int(multiplicacion(num1, num2)))
    elif (opcion == 4):
        print("\n", int(division(num1, num2)))
    elif (opcion == 5):
        print("\n", int(potencia(num1, num2)))
    elif (opcion == 6):
        print("\n", int(raiz(num1, num2)))

__main__()