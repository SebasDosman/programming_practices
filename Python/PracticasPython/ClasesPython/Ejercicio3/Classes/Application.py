class Application(object):
    copies_number = []
    
    def __init__(self, copies_number : list):
        self.copies_number = copies_number
    
    def register_article(self):
        return "Registering article"
    
    def register_client(self):
        return "Registering client"
    
    def sell(self):
        return "Selling"