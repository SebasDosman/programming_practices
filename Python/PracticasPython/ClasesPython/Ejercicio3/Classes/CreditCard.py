from Card import Card

class CreditCard(Card):
    def __init__(self, card_number : int, denomination : str, expiration_date : str):
        super().__init__(card_number, denomination, expiration_date)