from Dispensing import Dispensing

class Free(Dispensing):
    def __init__(self, price : int, name : str, expiration_date : str, start_date : str, end_date : str):
        super().__init__(price, name, expiration_date, start_date, end_date)