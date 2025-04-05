class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self): # Contrutor
        self.top = None
        self.size = 0


        

    def __len__(self):
        return self.size
    
    def __repr__(self):
        r = ""
        pointer = self.head
        while(pointer):
            r = r + str(pointer.data) + "->"
            pointer = pointer.next
        return r
    
    def __str(self):
        return self.__repr__()
    
