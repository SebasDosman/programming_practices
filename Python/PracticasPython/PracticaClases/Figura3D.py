from FiguraGeometrica import FiguraGeometrica

class Figura3D(FiguraGeometrica):
    caras = 0
    
    def __init__(self, vertices, caras):
        super().__init__(vertices)
        self.caras = caras
    
    def __get_caras__(self):
        return self.caras
    
    def __set_caras__(self, caras):
        self.caras = caras
    
    def __calcularVolumen__(self):
        return 0