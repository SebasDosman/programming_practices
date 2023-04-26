# from Client import Client
from typing import List

class Article(object):
    price = 0
    name = ""
    
    def __init__(self, price : int, name : str):
        self.price = price
        self.name = name
        # self.client = List[Client]
    
    def sell(self):
        return "Selling"