# Importaciones de librerías y módulos
import random
from Apartamento import Apartamento
from matrices import main

# Llamado al main de matrices.py para que se ejecute el programa
main(apartamento = Apartamento(random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)))