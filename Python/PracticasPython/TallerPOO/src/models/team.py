class Team:
    def __init__(self, id, code, name, group):
        self._id = id
        self._code = code
        self._name = name
        self._group = group
    
    @property
    def id(self):
        return self._id
    
    @property
    def code(self):
        return self._code
    
    @property
    def name(self):
        return self._name
    
    @property
    def group(self):
        return self._group
    
    @id.setter
    def id(self, id):
        self._id = id
    
    @code.setter
    def code(self, code):
        self._code = code
    
    @name.setter
    def name(self, name):
        self._name = name
    
    @group.setter
    def group(self, group):
        self._group = group
    
    def __str__(self):
        return f"{self._code} - {self._name} - {self._group}"