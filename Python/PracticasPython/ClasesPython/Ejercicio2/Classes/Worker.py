from People import People

class Worker(People):
    start_date = ""

    def __init__(self, id : int, name : str, start_date : str):
        super().__init__(id, name)
        self.start_date = start_date