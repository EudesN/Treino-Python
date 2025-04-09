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
        else:
            #primeira inserção
            self.head = Node(elem)
Lista = LinkedList()