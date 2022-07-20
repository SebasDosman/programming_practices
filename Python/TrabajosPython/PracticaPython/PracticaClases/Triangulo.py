from Figura2D import Figura2D

class Triangulo(Figura2D):
    base = 0
    altura = 0
    
    def __init__(self, base, altura, vertices = 3, lados = 3):
        super().__init__(vertices, lados)
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
        
    def __calcularArea__(self):
        print("Area" , int((self.base * self.altura) / 2))
    
    def __calcularPerimetro__(self):
        perimetro = 0
        
        for i in range(self.lados):
            medida = int(input("Digite la medida del lado \n"))
            perimetro = perimetro + medida
        
        print("Perimetro: " , perimetro)