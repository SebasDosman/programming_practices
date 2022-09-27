class Book(object):
    name = ""
    author = ""
    publisher = ""
    year = 0
    
    def __init__(self, name, author, publisher, year):
        self.name = name
        self.author = author
        self.publisher = publisher
        self.year = year
    
    def __getName__(self):
        return self.name
    
    def __setName__(self, name):
        self.name = name
    
    def __getAuthor__(self):
        return self.author
    
    def __setAuthor__(self, author):
        self.author = author
    
    def __getPublisher__(self):
        return self.publisher
    
    def __setPublisher__(self, publisher):
        self.publisher = publisher
    
    def __getYear__(self):
        return self.year
    
    def __setYear__(self, year):
        self.year = year
    
    def __toString__(self):
        print("Name: ", self.name, " | Author: ", self.author, " | Publisher: ", self.publisher, " | Year: ", self.year)