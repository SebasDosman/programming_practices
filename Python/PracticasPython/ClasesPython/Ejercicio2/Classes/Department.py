from Worker import Worker
from UndergraduateStudent import UndergraduateStudent

class Department(object):
    name = ""

    def __init__(self, name : str):
        self.name = name
        self.worker = Worker(0, "", "")
        self.undergraduate_student = UndergraduateStudent(0, "", "")