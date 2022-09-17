from abc import abstractmethod
from FiguraGeometrica import FiguraGeometrica

class Figura2D(FiguraGeometrica):
    lados = 0
    
    @abstractmethod
    def __init__(self, vertices, lados):
        super().__init__(vertices)
        self.lados = lados
        
    @abstractmethod
    def __get_lados__(self):
        return self.lados
    
    @abstractmethod
    def __set_lados__(self, lados):
        self.lados = lados
    
    @abstractmethod
    def __calcularPerimetro__(self):
        return 0
    