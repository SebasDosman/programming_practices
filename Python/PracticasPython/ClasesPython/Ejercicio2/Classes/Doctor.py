from Worker import Worker

class Doctor(Worker):
    def __init__(self, id : int, name : str, start_date : str):
        super().__init__(id, name, start_date)