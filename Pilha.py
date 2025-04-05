class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self): # Contrutor
        self.top = None
        self.size = 0


    def push(self, elemento): # insere um elemento na pilha
        node  = Node(elemento)
        node.next = self.top # o elemento abaixo na pilha é o que antes estava no topo
        self.top = node  # o novo topo é o nó que chega
        self.size = self.size + 1
        

    def pop(self): # remove o elemento do topo
        if self.size > 0:
            node = self.top
            self.top = self.top.next
            self.size = self.size - 1
            return node
        print("A pilha está vazia")

    def peek(self): # retorna o elemento do topo da pilha sen remover
        if self.size > 0:
            return self.top.data
        print("A pilha está vazia")

    def __len__(self):
        return self.size
    
    def __repr__(self):
        r = ""
        pointer = self.top
        while(pointer):
            r = r + str(pointer.data) + "\n"
            pointer = pointer.next
        return r
    
    def __str(self):
        return self.__repr__()
    
p