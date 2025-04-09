class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 

class LinkedList: # Não temos acesso direto aos elementos da lista. É necessário percorrer a lista a partir do início(cabeça).
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

    def replace(self, index): #subtitui um elemento por outro
        pointer = self.head
        pos = 0
        encontrado = False

        while pointer:
            if(pointer.data == index):
                print(f"valor {index} encontrado na posição {pos}")
                novo = input("Informe o valor a ser subtituido: ")
                pointer.data = novo
                encontrado = True
                break
            pointer = pointer.next
            pos += 1
        if not encontrado:
            print(f"O valor {index} não foi encontrado na lista")

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
    print("4- Substituir valor")
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
    elif(opcao == 4):
        index = input("Qual elemento deseja subtituir? ")
        Lista.replace(index)
    elif(opcao == 0):
        print("Encerrando...")
        break