#Importando clase desde otro archivo
from Animal import Animal 

#Clase
class Perro(Animal):
    numeroPulgas = 0 
    
    #Constructor
    def  __init__(self, numeroPatas, estiloDesplazamiento, edad, nombre, duenio, numeroPulgas):
        super().__init__(numeroPatas, estiloDesplazamiento, edad, nombre, duenio)
        self.numeroPulgas = numeroPulgas
        
    #Getter y Setter
    @property
    def __get_numeroPulgas__(self):
        return self.numeroPulgas
    
    @property
    def __set_numeroPulgas(self, numeroPulgas):
        self.numeroPulgas = numeroPulgas
    
    def __ladrar__(self):
        print("Wow, wow")
    
perro = Perro(4, "Camina", 12, "Floppy", "Kelly", 10)
print(perro.__get_nombre__())
perro.__ladrar__()