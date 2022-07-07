from webbrowser import get
from FiguraGeometrica import FiguraGeometrica

class Figura2D(FiguraGeometrica):
    lados = 0
    
    def __init__(self, vertices, lados):
        super().__init__(vertices)
        self.lados = lados
        
    def __get_lados__(self):
        return self.lados
    
    def __set_lados__(self, lados):
        self.lados = lados
    
    def __calcularPerimetro__(self):
        return 0
    