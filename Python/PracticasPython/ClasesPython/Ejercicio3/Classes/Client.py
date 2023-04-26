from Article import Article
from typing import List
from Card import Card
from Contact import Contact
from People import People

class Client(People):
    id = 0
    RUC = ""
    address = ""    
    
    def __init__(self, name : str, last_name : str, birth_date : str, id : int, RUC : int, address : str):
        super().__init__(name, last_name, birth_date)
        self.id = id
        self.RUC = RUC
        self.address = address
        self.cards = List[Card]
        self.contacts = List[Contact]
        self.articles = List[Article]
    
    def buy(self):
        return "Buying"