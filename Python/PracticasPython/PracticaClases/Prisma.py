import math

from Figura3D import Figura3D

class Prisma(Figura3D):
    base = 0
    altura = 0
    
    def __init__(self, base, altura, vertices = 4, caras = 4):
        super().__init__(vertices, caras)
        self.base = base
        self.altura = altura
    
    def __get_base__(self):
        return self.base
    
    def __set_base__(self, base):
        self.base = base
        
    def __get_altura__(self):
        return self.altura
    
    def __set_altura__(self, altura):
        self.altura = altura
        
    def  __calcularArea__(self):
        print("Area: " , int((self.base * 2) * ((self.base * self.altura )/ 2)) )      
    
    def  __calcularVolumen__(self):
        print("Volumen: " , int((1 / 3) * math.pow(self.base, 2) * self.altura))       