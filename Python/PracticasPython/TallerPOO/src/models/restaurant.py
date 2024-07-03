class Restaurant:
    def __init__(self, id, name, products, id_stadium):
        self._id = id
        self._name = name
        self._products = products
        self._id_stadium = id_stadium
    
    @property	
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    @property
    def products(self):
        return self._products
    
    @property
    def id_stadium(self):
        return self._id_stadium
    
    @id.setter
    def id(self, id):
        self._id = id
    
    @name.setter
    def name(self, name):
        self._name = name
    
    @products.setter
    def products(self, products):
        self._products = products
    
    @id_stadium.setter
    def id_stadium(self, id_stadium):
        self._id_stadium = id_stadium
    
    def __str__(self):
        return f"{self._name} - {self._products} - {self._id_stadium}"