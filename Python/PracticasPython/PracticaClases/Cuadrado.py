from Figura2D import Figura2D

class Cuadrado(Figura2D):    
    medidaLado = 0
    
    def __init__(self, medidaLado, vertices = 4, lados = 4):
        super().__init__(vertices, lados)
        self.medidaLado = medidaLado
        
    def __get_medidaLado__(self):
        return self.medidaLado
    
    def __set_medidaLado__(self, medidaLado):
        self.medidaLado = medidaLado
        
    def __calcularArea__(self):
        print("Area: " , int(self.medidaLado * self.medidaLado))
    
    def __calcularPerimetro__(self):
        print("Perimetro: " , int(self.medidaLado * 4))