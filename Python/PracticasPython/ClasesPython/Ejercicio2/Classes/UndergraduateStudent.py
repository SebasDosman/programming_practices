from Student import Student

class UndergraduateStudent(Student):
    tittle = ""

    def __init__(self, id : int, name : str, tittle : str):
        super().__init__(id, name)
        self.tittle = tittle
    
    def collaborate(self):
        return "Collaborating"