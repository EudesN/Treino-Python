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
        self.size += 1
    def __repr__(self):
        if self.empty():
            return 'A fila está vazia'

        exibirLista = ""
        pointer = self.head

        while pointer:
            exibirLista += str(pointer.data)
            pointer = pointer.next
            if(pointer):
                exibirLista += " -> "
            
        return exibirLista

    def __len__(self):
        return self.size

    def empty(self):
        return self.size == 0


Lista = LinkedList()
while True:
    print("-"* 30)
    print("1- Adicionar elemento a lista")
    print("2- Exibir lista")
    print("3- Monstrar tamanho da lista")
    print("0- Sair")
    print("-"* 30)
    opcao = int(input("Informe a opcão: "))

    if(opcao == 1):
        n = input("Informe o elemento: ")
        Lista.append(n)
    elif(opcao == 2):
        print(f"Lista: {Lista.__repr__()}")
    elif(opcao == 3):
        print(f"A lista possui {Lista.__len__()} elementos")
    elif(opcao == 0):
        print("Encerrando...")
        break