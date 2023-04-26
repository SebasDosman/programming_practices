class Manager(object):
    id = 0
    name = ""
    phone_number = 0
    location = ""

    def __init__(self, id : int, name : str, phone_number : int, location : str):
        self.id = id
        self.name = name
        self.phone_number = phone_number
        self.location = location
    
    def purchase_inventory(self):
        return "Purchasing inventory" 
    
    def record_complaints(self):
        return "Recording complaints"
    
    def manage_staff(self):
        return "Managing staff"