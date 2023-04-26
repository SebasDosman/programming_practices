from Department import Department

class University():
    name = ""
    city = ""
    
    def __init__(self, name : str, city : str, department : Department):
        self.name = name
        self.city = city
        self.department = department
