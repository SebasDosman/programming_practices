class Node():
    def __init__(self):
        self.info, self.sig = None, None  

class Stack():
    def __init__(self):
        self.top, self.length = None, 0
    
    def __dequeue__(self):
        top = self.top
        
        removedNode = self.top.sig
        self.top = removedNode
        
        self.length -= 1
        return top
    
    def __enqueue__(self, node : Node):
        if (self.length == 0):
            self.top = node
        else:
            previous = self.top
            self.top = node
            previous.sig = self.top
        
        self.length += 1
    
    def __emptyStack__(self):
        if (self.length == 0):
            return True
        else:
            return False
    
    def __top__(self):
        return self.top.info
    
    def __length__(self):
        return self.length

