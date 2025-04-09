class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __append(self, elem):
        if self.head:
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(elem)
        else:
            #primeira inserção
            self.head = Node(elem)


Lista = LinkedList()
while True:
    print("1- Adicionar elemento a lista")
    print("2- Exibir lista")
    print("0- Sair")
