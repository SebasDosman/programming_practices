from Drug import Drug

class Dispensing(Drug):
    start_date = ""
    end_date = ""
    
    def __init__(self, price : int, name : str, expiration_date : str, start_date : str, end_date : str):
        super().__init__(price, name, expiration_date)
        self.start_date = start_date
        self.end_date = end_date

