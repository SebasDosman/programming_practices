import math
from Figura3D import Figura3D

class Esfera(Figura3D):
    radio = 0
    
    def __init__(self, radio, vertices = 0, caras = 1):
        super().__init__(vertices, caras)
        self.radio = radio
        
    def __get_radio__(self):
        return self.radio
    
    def __set_radio__(self, radio):
        self.radio = radio
        
    def __calcularArea__(self):
        print("Area: " , int(4 * math.pi * math.pow(self.radio, 2)))
    
    def __calcularVolumen__(self):
        print("Volumen: " , int((4 / 3) * math.pi * math.pow(self.radio, 3)))