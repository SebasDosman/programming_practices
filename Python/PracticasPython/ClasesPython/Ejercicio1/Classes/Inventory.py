class Inventory(object):
    type = ""
    status = ""

    def __init__(self, type : str, status : str):
        self.type = type
        self.status = status