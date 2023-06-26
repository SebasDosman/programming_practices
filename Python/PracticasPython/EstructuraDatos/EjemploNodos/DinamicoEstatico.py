# <-- Estatico --> 
n1 = 10
n2 = n1
n2 = n2 + 15
# print("Valor n1 : " , n1 , "| Valor n2 : " , n2)
# Van a diferentes espacios de memoria porque solo se estan utilizando o inicializando variables con un valor cualquiera


# <-- Dinamico -->
l1 = [ 5 , 10 , 15 ]
l2 = l1
l2 [ 1 ] = 50
l2.append ( 150 )
# print ("Valor l1 : " , l1 , "| Valor l2 : " , l2 )
# Aqui se mueve lo mismo en l1 como en l2 ya que se estan usando estructuras que usan "index" en este caso, una lista


# <-- Puntero -->
p1 = [0, 1]
p2 = [0, 1]

print (id(p1))
print (id(p2))

if (p1 is p2):
    print ("p1 y p2 apuntan a la misma variable dinamica")
else:    
    print ("p1 y p2 apuntan a diferente variable dinamica")
    
p1 = {}
p2 = p1

print (id(p1))
print (id(p2))       

if (p1 is p2):
    print ("p1 y p2 apuntan a la misma variable dinamica")
else:    
    print ("p1 y p2 apuntan a diferente variable dinamica")  