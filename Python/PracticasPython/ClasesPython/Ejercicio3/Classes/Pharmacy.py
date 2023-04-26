from Article import Article
from Company import Company
from People import People
from Provider import Provider
from typing import List

class Pharmacy(Company):
    def __init__(self):
        super().__init__()
        self.articles = List[Article]
        self.clients = List[People]
        self.providers = List[Provider]
    
    def sell(self):
        return "buying"
    
    def restock(self):
        return "restocking"
