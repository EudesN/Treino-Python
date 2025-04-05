class Node:
    def __init__(self):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def push(self, elemento):
        node = Node(elemento)
        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node
        
        if self.first is None:
            self.first = node
        else:
            self.first = node

        self.size += 1
    
    def __len__(self):
        return self.size
    
    def empty(self):
        return len(self) == 0 # retorna True quando vazio




