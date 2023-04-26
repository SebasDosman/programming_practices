# Importaciones de librerías y módulos
from array import array
from Apartamento import Apartamento

# Función que recibe una matriz y un objeto de la clase Apartamento y retorna 
# la cantidad de personas, litros de agua y consumo de energía en una lista de tres 
# posiciones con la función sum
def matriz_por_cuatro(matriz : array, objeto : Apartamento):
    for i in range(4):
        matriz.append(objeto)
    
    return [sum(matriz.get_personas() for matriz in matriz), sum(matriz.get_litros_agua() for matriz in matriz), sum(matriz.get_consumo_energia() for matriz in matriz)]

# Función que llama a la función matriz_por_cuatro 5 veces y retorna la cantidad de personas,
def matriz_por_cinco(matriz : array, objeto : Apartamento):
    for i in range(5):
        count = matriz_por_cuatro(matriz, objeto)
    
    return count

# Función que llama a la función matriz_por_cinco 8 veces y retorna la cantidad de personas,
def matriz_por_ocho(matriz : array, objeto : Apartamento):
    for i in range(8):
        count = matriz_por_cinco(matriz, objeto)
    
    return count

# Función que llama a la función matriz_por_ocho 2 veces y retorna la cantidad de personas,
def matriz_por_dos(matriz : array, objeto : Apartamento):
    for i in range(2):
        count = matriz_por_ocho(matriz, objeto)
    
    return count

# Función que llama a la función matriz_por_dos 3 veces y retorna la cantidad de personas,
def matriz_por_tres(matriz : array, objeto : Apartamento):
    for i in range(3):
        count = matriz_por_dos(matriz, objeto)
    
    return count

# Función main que llama a la función matriz_por_tres y retorna la cantidad de personas, 
# litros de agua y consumo de energía y las imprime en pantalla
def main(apartamento : Apartamento):
    casas : array = []
    count : int = 0

    count = matriz_por_tres(casas, apartamento)
    print("Cantidad de personas: " , count[0])
    print("Cantidad de litros de agua: " , count[1])
    print("Cantidad de consumo de energía: " , count[2])