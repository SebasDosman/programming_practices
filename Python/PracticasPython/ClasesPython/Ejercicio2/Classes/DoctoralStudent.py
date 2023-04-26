from Student import Student

class DoctoralStudent(Student):
    program = ""

    def __init__(self, id : int, name : str, program : str):
        super().__init__(id, name)
        self.program = program
    
    def start_test(self):
        return "Starting test"