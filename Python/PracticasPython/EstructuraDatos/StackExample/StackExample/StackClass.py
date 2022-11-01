class Node(object):
    info, next = None, None

class Stack(object):
    def __init__(self):
        self.top = None
        self.length = 0
    
    def __stack__(self, data):
        node = Node()
        node.info = data
        node.next = self.top
        self.top = node
        self.length += 1
    
    def __unstack__(self):
        infoTop = self.top.info
        self.top = self.top.next
        self.length -= 1
        return infoTop
    
    def __emptyStack__(self):
        return self.top is None
    
    def __inTop__(self):
        if self.top is not None:
            return self.top.info
        else:
            return None
    
    def __length__(self):
        return self.length