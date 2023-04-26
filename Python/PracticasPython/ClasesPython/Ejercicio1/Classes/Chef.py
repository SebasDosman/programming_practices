class Chef(object):
    id = 0
    name = ""
    location = ""

    def __init__(self, id : int, name : str, location : str):
        self.id = id
        self.name = name
        self.location = location
    
    def take_orders(self):
        return "Taking orders"
