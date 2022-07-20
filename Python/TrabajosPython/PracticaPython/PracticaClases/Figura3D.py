from abc import abstractmethod
from FiguraGeometrica import FiguraGeometrica

class Figura3D(FiguraGeometrica):
    caras = 0
    
    @abstractmethod
    def __init__(self, vertices, caras):
        super().__init__(vertices)
        self.caras = caras
    
    @abstractmethod
    def __get_caras__(self):
        return self.caras
    
    @abstractmethod
    def __set_caras__(self, caras):
        self.caras = caras
    
    @abstractmethod
    def __calcularVolumen__(self):
        return 0