#Clase
class Persona():
    nombre = ""
    identificacion = 0
    edad = 0
    estatura = 0.0
    genero = ""
    
    #Constructor
    def __init__(self, nombre, identificacion, edad, estatura, genero):
        self.nombre = nombre
        self.identificacion = identificacion
        self.edad = edad
        self.estatura = estatura
        self.genero = genero
        
    #Getter y Setter
    def __get_nombre__(self):
        return self.nombre
    
    def __set_nombre__(self, nombre):
        self.nombre = nombre
        
    def __get_identificacion__(self):
        return self.identificacion
    
    def __set_identificacion__(self, identificacion):
        self.identificacion = identificacion
        
    def __get_edad__(self):
        return self.edad
    
    def __set_edad__(self, edad):
        self.edad = edad
        
    def __get_estatura__(self):
        return self.estatura
    
    def __set_estatura__(self, estatura):
        self.estatura = estatura
        
    def __get_genero__(self):
        return self.genero
    
    def __set_estatura__(self, genero):
        self.genero = genero
        
    def __saludar__(self, message):
        return message

#Instancia de una clase
persona1 = Persona("Sebastian", 1105362481, 17, 1.70, "Masculino")
# persona1.__set_edad__(18)
# print(persona1.__get_edad__())

mensaje = "Hola"
print(persona1.__saludar__(mensaje))