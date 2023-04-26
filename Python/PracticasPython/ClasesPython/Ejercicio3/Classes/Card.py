class Card(object):
    card_number = 0
    denomination = 0
    expiration_date = ""
    
    def __init__(self, card_number : int, denomination : int, expiration_date : str):
        self.card_number = card_number
        self.denomination = denomination
        self.expiration_date = expiration_date