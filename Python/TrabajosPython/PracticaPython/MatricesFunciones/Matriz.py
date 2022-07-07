#Funciones
def calcularSumatoria(h, num):
    sum = (number * num * h)
    return sum
    
def calcularPromedio(sum, cont):
    prom = (sum / cont) 
    return prom

def imprimirArchivo(sum, prom, matrix):
    print("\n")
    print(sum)
    print(prom)

    print("\n")
    print(matrix)
    
def llenarMatrix():
    sum = 0
    cont = 0
    contPares = 0
    
    for e in range(0, 2):
        for i in range(0, 5):
            for j in range(0, 4):
                for k in range(0, 7):
                    h = (e + i + j + k)
                    cont = cont + 1
                        
                    if (h % 2 == 0):
                        num = 2
                        sum = sum + calcularSumatoria(num, h)
                        matrix[e][i][j][k] = sum
                        contPares = contPares + 1
                    else:
                        num = 3
                        sum = sum + calcularSumatoria(num, h)
                        matrix[e][i][j][k] = sum  
    
    prom = calcularPromedio(sum, cont)
    imprimirArchivo(sum, prom, matrix)
    
    print("\n")
    print("Numeros Pares: ", contPares)
    
#Inicializacion Matrix
matrix = [[[[[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]]],
          [[[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]]],
          [[[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]]],
          [[[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]]],
          [[[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]]]],
          [[[[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]]],
          [[[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]]],
          [[[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]]],
          [[[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]]],
          [[[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]]]]]

max = int(input("Digite la cantidad de numeros a ingresar \n"))

#Cantidad De Repeticiones 
for m in range(max):
    number = int(input("\n Digite un numero \n"))
    llenarMatrix()