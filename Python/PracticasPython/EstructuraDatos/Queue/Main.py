class Node():
    def __init__(self):
        self.info, self.sig = None, None  

class Queue():
    def __init__(self):
        self.first, self.last, self.length = None, None, 0
    
    
    
    def __emptyQueue__(self):
        if (self.length == 0):
            return True
        else:
            return False
    
    def __inFront__(self):
        return self.first.info
    
    def __length__(self):
        return self.length