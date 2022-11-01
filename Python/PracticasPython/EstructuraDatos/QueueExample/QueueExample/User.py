from Request import Request
class User():
    name = ""
    lastName = ""
    age = 0
    document = 0
    request : Request = 0
    
    def __init__(self, name, lastName, age, document, request : Request):
        self.name = name
        self.lastName = lastName
        self.age = age
        self.document = document
        self.request = request
    
    def __getName__(self):
        return self.name
    
    def __setName__(self, name):
        self.name = name
        
    def __getLastName__(self):
        return self.lastName
    
    def __setLastName__(self, lastName):
        self.lastName = lastName
        
    def __getAge__(self):
        return self.age
    
    def __setAge__(self, age):
        self.age = age
    
    def __getDocument__(self):
        return self.document
    
    def __setDocument__(self, document):
        self.document = document
    
    def __getRequest__(self):
        return self.request
    
    def __setRequest__(self, request):
        self.request = request
    
    def __toString__(self):
        print("Name: ", self.name, "| Last Name: ", self.lastName, "| Age: ", self.age, "| Document: ", self.document, "| Request: ", self.request)