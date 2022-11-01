from User import User
from Request import Request

class Node(object):
    info, next = None, None

class Queue(object):
    def __init__(self):
        self.first, self.last = None, None
        self.length = 0
    
    def __enqueue__(self, data : User):
        node = Node()
        node.info = data
        
        if self.first is None:
            self.first = node
        else:
            self.last.next = node
        
        self.last = node
        self.length += 1
    
    def __dequeue__(self):
        self.first.info.__setRequest__(Request.SUCCESSFUL)
        
        data = self.first.info
        self.first = self.first.next
        
        if self.first is None:
            self.final = None
        
        self.length -= 1
        return data
    
    def __emptyQueue__(self):
        return self.first is None 
    
    def __inFront__(self):
        return self.first.info
    
    def __length__(self):
        return self.length
    
    def __moveToLast__(self):
        data = Queue.__dequeue__()
        Queue.__enqueue__(data)
        
        return data