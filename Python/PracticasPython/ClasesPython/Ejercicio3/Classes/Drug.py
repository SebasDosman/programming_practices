from Article import Article

class Drug(Article):
    expiration_date = ""
    
    def __init__(self, price : int, name : str, expiration_date : str):
        super().__init__(price, name)
        self.expiration_date = expiration_date
    
    def is_expired(self):
        return "Is expired?"