# Importamos la librería Numpy para poder convertir la nota que se recibe a un numero decimal
from numpy import double

# Definimos un arreglo para así guardar varias notas en una sola variable
arreglo_notas = []

# Definimos una variable acumulativa para poder acumular las notas y así sacar el promedio
acumulador = 0

# Igualamos una variable a la cantidad de notas que se va a recibir, esta cantidad debe ser un entero, por eso se usa la función int()
cant_notas = int(input("Digite la cantidad de notas \n"))

# Usamos un ciclo que va desde la posición 0 hasta la cantidad de notas que nos dijo el usuario va a digitar
for i in range(0, cant_notas):
    # Igualamos una variable a la nota que se va a recibir, esta nota debe ser un decimal, por eso se usa la función double()
    nota = double(input("Digite la nota \n"))
    # Agregamos esta nota al arreglo de las notas con la función propia de los arreglos append(), esta función me agrega un valor al final del arreglo
    arreglo_notas.append(nota)

# Buscamos la menor nota dentro del arreglo de notas con la función min() e igualamos una variable a ese valor
minimo = min(arreglo_notas)

# Ahora debemos buscar la posición en la que se encuentra dicho valor, por eso usamos un atributo de los arreglos llamado index y le pasamos la nota a buscar
indice_min = arreglo_notas.index(minimo)

# Ahora sacamos la nota minima del arreglo para así favorecer al estudiante
arreglo_notas.pop(indice_min)

# Usamos otro ciclo para recorrer el arreglo ya con la nota menor habiendo sido eliminada, este ciclo va desde 0 hasta el tamaño del arreglo, por eso usamos la función len()
for j in range(0, len(arreglo_notas)):
    
    # Empezamos a utilizar la variable acumulativa, esta variable me va acumulando las notas que se encuentran en cada posición del arreglo para poder sacar el promedio de las mismas
    acumulador += arreglo_notas[j]

# Igualamos una variable a la suma de las notas divididas entre la cantidad de las mismas, que corresponde a la formula del promedio
promedio = (acumulador / len(arreglo_notas))

# Por último imprimimos en pantalla el promedio
print("El promedio de las notas es: ", promedio)