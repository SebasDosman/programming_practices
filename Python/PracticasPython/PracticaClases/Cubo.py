import math

from Figura3D import Figura3D

class Cubo(Figura3D):
    medidaLado = 0
    
    def __init__(self, medidaLado, vertices = 8, caras = 6):
        super().__init__(vertices, caras)
        self.medidaLado = medidaLado
        
    def __get_medidaLado__(self):
        return self.medidaLado
    
    def __set_medidaLado__(self, medidaLado):
        self.medidaLado = medidaLado
        
    def __calcularArea__(self):
        print("Area: " , int(6 * math.pow(self.medidaLado, 2)))
    
    def __calcularVolumen__(self):
        print("Volumen: " , int(math.pow(self.medidaLado, 3)))