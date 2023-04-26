from Worker import Worker

class PAS(object):
    position = ""
    
    def __init__(self, position : str, worker :  Worker):
        self.position = position
        self.worker = worker
    
    def manage(self):
        return "Managing"