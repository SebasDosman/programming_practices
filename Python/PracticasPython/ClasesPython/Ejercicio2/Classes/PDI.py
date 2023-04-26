from Worker import Worker

class PDI(object):
    category = ""
    
    def __init__(self, category : str, worker : Worker):
        self.category = category
        self.worker = worker
    
    def investigate(self):
        return "Investigating"
    
    def teach(self):
        return "Teaching"