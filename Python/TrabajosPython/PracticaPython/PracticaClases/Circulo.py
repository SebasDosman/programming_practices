import math
from Figura2D import Figura2D

class Circulo(Figura2D):
    radio = 0
    
    def __init__(self, radio, vertices = 0, lados = 0):
        super().__init__(vertices, lados)
        self.radio = radio
        
    def __get_radio__(self):
        return self.radio
    
    def __set_radio__(self, radio):
        self.radio = radio
        
    def __calcularArea__(self):
        print("Area: " , int(math.pi * math.pow(self.radio, 2)))
    
    def __calcularPerimetro__(self):
        print("Perimetro: " , int(self.radio * 2 * math.pi))