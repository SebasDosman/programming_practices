class HouseKeeping(object):
    id = 0
    name = ""
    location = ""

    def __init__(self, id : int, name : str, location : str):
        self.id = id
        self.name = name
        self.location = location
    
    def clean_room(self):
        return "Cleaning room"