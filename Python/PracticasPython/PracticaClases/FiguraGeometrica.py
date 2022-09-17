from abc import abstractmethod

class FiguraGeometrica():
    vertices = 0
    
    @abstractmethod
    def __init__(self, vertices):
        self.vertices = vertices
    
    @abstractmethod
    def __get_vertices__(self):
        return self.vertices
    
    @abstractmethod
    def __set_vertices__(self, vertices):
        self.vertices = vertices
    
    @abstractmethod
    def __calcularArea__(self):
        return 0