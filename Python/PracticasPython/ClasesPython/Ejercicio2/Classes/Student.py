from People import People

class Student(People):
    def __init__(self, id : int, name : str):
        super().__init__(id, name)