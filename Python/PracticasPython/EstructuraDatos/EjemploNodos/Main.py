from Polinomio import Nodo, datoPolinomio, Polinomio, agregar_termino, obtener_valor, mostrar, sumar

poli1 = Polinomio()
agregar_termino(poli1, 2, -3)
agregar_termino(poli1, 3, 2)
agregar_termino(poli1, 1, 4)
print ("POLINOMIO 1:")
print (mostrar(poli1))


poli2 = Polinomio()
agregar_termino(poli2, 2, 2)
agregar_termino(poli2, 0, 3)
print ("POLINOMIO 2:")
print (mostrar(poli2))


print ("POLINOMIO 1 + POLINOMIO 2:")
print (mostrar(sumar(poli1,poli2)))   