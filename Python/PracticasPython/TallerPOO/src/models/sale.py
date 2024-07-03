class Sale:
    def __init__(self, id, dni_client, products, amount):
        self._id = id
        self._dni_client = dni_client
        self._products = products
        self._amount = amount
    
    @property
    def id(self):
        return self._id
    
    @property
    def dni_client(self):
        return self._dni_client
    
    @property
    def products(self):
        return self._products
    
    @property
    def amount(self):
        return self._amount
    
    @id.setter
    def id(self, id):
        self._id = id
    
    @dni_client.setter
    def dni_client(self, dni_client):
        self._dni_client = dni_client
    
    @products.setter
    def products(self, products):
        self._products = products
    
    @amount.setter
    def amount(self, amount):
        self._amount = amount
    
    def __str__(self):
        return f"{self._dni_client} - {self._products} - {self._amount}"
