from random import randint, random

class Array:
    def __init__(self, capacity, fill_value = None):
        self.items = list()
        
        for i in range(capacity):
            self.items.append(fill_value)
            
    def __len__(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
    def __iter__(self):
        return iter(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __setitem__(self, index, value):
        self.items[index] = value
        
    def __set_random__(self):
        for i in range(len(self)):
            self.items[i] = randint(0, 10)
        
    def __set_sum__(self):
        result = 0
        
        for i in range(len(self)):
            result += self.items[i]
            
        return result
        
array = Array(10, 0)
print(array)

array.__set_random__()
print(array)

print(array.__set_sum__())