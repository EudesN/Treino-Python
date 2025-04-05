class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def enqueue(self, elemento): # adiciona no final da fila
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

    def dequeue(self): # retira o primeiro da fila
        if self.first:
            removed = self.first
            self.first = self.first.next
            if self.first is None:
                self.last = None # fila ficou vazia
            self.size -= 1
            return removed.data
        print('A fila está vazia.')

    def peek(self): #monstra o primeiro elemento
        if self.first:
            return self.first.data
        print("Não há primeiro elemento. A fila está vazia. ")

    def __repr__(self):
        if self.empty():
            return 'Fila vazia'
        s = ''
        pointer = self.first
        while(pointer):
            s += str(pointer.data)
            pointer = pointer.next
            if(pointer):
                s+= ' -> '
        return s

    def __len__(self):
        return self.size
    
    def empty(self):
        return len(self) == 0 # retorna True quando vazio

fila = Queue()


