# Clase Apartamento con los atributos personas, litros_agua y consumo_energia 
# y sus métodos get y set para cada atributo 

class Apartamento(object):
    def __init__(self, personas, litros_agua, consumo_energia):
        self.personas = personas
        self.litros_agua = litros_agua
        self.consumo_energia = consumo_energia
    
    def get_personas(self):
        return self.personas
    
    def set_personas(self, personas):
        self.personas = personas
    
    def get_litros_agua(self):
        return self.litros_agua
    
    def set_litros_agua(self, litros_agua):
        self.litros_agua = litros_agua
    
    def get_consumo_energia(self):
        return self.consumo_energia
    
    def set_consumo_energia(self, consumo_energia):
        self.consumo_energia = consumo_energia