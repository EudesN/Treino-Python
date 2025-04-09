class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, elem):
        if self.head:
            #inserção quando a lista já tem elementos
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(elem)
        else:
            #primeira inserção
            self.head = Node(elem)
    def __repr__(self):
        exibirLista = ""
        pointer = self.head
        while pointer:
            exibirLista += str(pointer.data)
            pointer = pointer.next
            if(pointer):
                exibirLista += " -> "
            
        return exibirLista


Lista = LinkedList()
while True:
    print("1- Adicionar elemento a lista")
    print("2- Exibir lista")
    print("0- Sair")
    opcao = int(input("Informe a opcão: "))

    if(opcao == 1):
        n = input("Informe o elemento: ")
        Lista.append(n)
    elif(opcao == 2):
        print(Lista.__repr__())
    elif(opcao == 0):
        print("Encerrando...")
        break