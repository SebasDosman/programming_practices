class Product:
    def __init__(self, id, name, classification, is_alcohol, aliment_type, price, inventory, id_restaurant):
        self._id = id
        self._name = name
        self._classification = classification
        self._is_alcohol = is_alcohol 
        self._aliment_type = aliment_type
        self._price = price
        self._inventory = inventory
        self._id_restaurant = id_restaurant
    
    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    @property
    def classification(self):
        return self._classification
    
    @property
    def is_alcohol(self):
        return self._is_alcohol
    
    @property
    def aliment_type(self):
        return self._aliment_type
    
    @property
    def price(self):
        return self._price
    
    @property
    def inventory(self):
        return self._inventory
    
    @property
    def id_restaurant(self):
        return self._id_restaurant
    
    @id.setter
    def id(self, id):
        self._id = id
    
    @name.setter
    def name(self, name):
        self._name = name
    
    @classification.setter
    def classification(self, classification):
        self._classification = classification
    
    @is_alcohol.setter
    def is_alcohol(self, is_alcohol):
        self._is_alcohol = is_alcohol
    
    @aliment_type.setter
    def aliment_type(self, aliment_type):
        self._aliment_type = aliment_type
    
    @price.setter
    def price(self, price):
        self._price = price
    
    @inventory.setter
    def inventory(self, inventory):
        self._inventory = inventory
    
    @id_restaurant.setter
    def id_restaurant(self, id_restaurant):
        self._id_restaurant = id_restaurant
    
    def __str__(self):
        return f"{self._name} - {self._classification} - {self._is_alcohol} - {self._aliment_type} - {self._price} - {self._inventory} - {self._id_restaurant}"