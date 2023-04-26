class People(object):
    name = ""
    last_name = ""
    birth_date = ""
    
    def __init__(self, name : str, last_name : str, birth_date : str):
        self.name = name
        self.last_name = last_name
        self.birth_date = birth_date