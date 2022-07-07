#Clase
class Animal():
    numeroPatas = 0
    estiloDesplazamiento = ""
    edad = 0
    nombre = ""
    duenio = ""
    
    #Constructor
    def __init__(self, numeroPatas, estiloDesplazamiento, edad, nombre, duenio):
        self.numeroPatas = numeroPatas
        self.estiloDesplazamiento = estiloDesplazamiento
        self.edad = edad
        self.nombre = nombre
        self.duenio = duenio
        
    #Getter y Setter
    def __get_numeroPatas__(self):
        return self.numeroPatas
    
    def __set_numeroPatas__(self, numeroPatas):
        self.numeroPatas = numeroPatas
        
    def __get_estiloDesplazamiento__(self):
        return self.estiloDesplazamiento
    
    def __set_estiloDesplazamiento__(self, estiloDesplazamiento):
        self.estiloDesplazamiento = estiloDesplazamiento
        
    def __get_edad__(self):
        return self.edad
    
    def __set_edad__(self, edad):
        self.edad = edad
        
    def __get_nombre__(self):
        return self.nombre
    
    def __set_nombre__(self, nombre):
        self.nombre = nombre
        
    def __get_duenio__(self):
        return self.duenio
    
    def __set_duenio__(self, duenio):
        self.duenio = duenio
        
    def __crecer__(self):
        self.edad = self.edad + 1
        
#Instancias de la clase
perro = Animal(4, "Camina", 12, "Floppy", "Kelly")
caballo = Animal(4, "Trota", 10, "Trochadora", "Andres")
pez = Animal(0, "Nada", 2, "Nemo", "Dory")