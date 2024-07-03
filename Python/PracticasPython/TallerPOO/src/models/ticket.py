class Ticket:
    def __init__(self, id, dni_client, name_client, age_client, type, seat, available, id_match, price):
        self._id = id
        self._dni_client = dni_client
        self._name_client = name_client
        self._age_client = age_client
        self._type = type
        self._price = price
        self._seat = seat
        self._available = available
        self._id_match = id_match
    
    @property
    def id(self):
        return self._id
    
    @property
    def dni_client(self):
        return self._dni_client
    
    @property
    def name_client(self):
        return self._name_client
    
    @property
    def age_client(self):
        return self._age_client
    
    @property
    def type(self):
        return self._type
    
    @property
    def price(self):
        return self._price
    
    @property
    def seat(self):
        return self._seat
    
    @property
    def available(self):
        return self._available
    
    @property
    def id_match(self):
        return self._id_match
    
    @id.setter
    def id(self, id):
        self._id = id
    
    @dni_client.setter
    def dni_client(self, dni_client):
        self._dni_client = dni_client
    
    @name_client.setter
    def name_client(self, name_client):
        self._name_client = name_client
    
    @age_client.setter
    def age_client(self, age_client):
        self._age_client = age_client
    
    @type.setter
    def type(self, type):
        self._type = type
    
    @price.setter
    def price(self, price):
        self._price = price
    
    @seat.setter
    def seat(self, seat):
        self._seat = seat
    
    @available.setter
    def available(self, available):
        self._available = available
    
    @id_match.setter
    def id_match(self, id_match):
        self._id_match = id_match
    
    def __str__(self):
        return f"{self._dni_client} - {self._name_client} - {self._age_client} - {self._type} - {self._price} - {self._seat} - {self._available} - {self._id_match}"
    
    def to_dict(self):
        return {"id": self._id,"dni_client": self._dni_client,"name_client": self._name_client,"age_client": self._age_client,"type": self._type,"price": self._price,"seat": self._seat,"available": str(self._available).lower(),"id_match": self._id_match}