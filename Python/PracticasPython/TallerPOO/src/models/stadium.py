class Stadium:
    def __init__(self, id, name, location):
        self._id = id
        self._name = name
        self._location = location
    
    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    @property
    def location(self):
        return self._location
    
    @id.setter
    def id(self, id):
        self._id = id
    
    @name.setter
    def name(self, name):
        self._name = name
    
    @location.setter
    def location(self, location):
        self._location = location
    
    def __str__(self):
        return f"{self._name} - {self._location}"