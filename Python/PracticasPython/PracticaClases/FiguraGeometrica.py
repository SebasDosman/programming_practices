class FiguraGeometrica():
    vertices = 0
    
    def __init__(self, vertices):
        self.vertices = vertices
    
    def __get_vertices__(self):
        return self.vertices
    
    def __set_vertices__(self, vertices):
        self.vertices = vertices
    
    def __calcularArea__(self):
        return 0