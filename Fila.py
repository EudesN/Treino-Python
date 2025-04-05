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
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self.size += 1

    def dequeue(self): # retira o primeiro da fila
        if self.first:
            removed = self.first.data
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

while True:
    print("\n========== MENU DA FILA ==========")
    print("1 - Adicionar elemento (enqueue)")
    print("2 - Remover elemento (dequeue)")
    print("3 - Mostrar fila")
    print("4 - Mostrar primeiro da fila (peek)")
    print("5 - Mostrar quantidade de elementos")
    print("0 - Sair")
    print("===================================")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = input("Digite o valor para adicionar na fila: ")
        fila.enqueue(valor)
        print(f'"{valor}" adicionado à fila.')

    elif opcao == "2":
        removed = fila.dequeue()
        print(f"Elemento removido: {removed}")

    elif opcao == "3":
        print("Fila atual:")
        print(__re)

    elif opcao == "4":
        print("Primeiro da fila:", fila.peek())

    elif opcao == "5":
        print("Quantidade de elementos na fila:", len(fila))

    elif opcao == "0":
        print("Encerrando o programa.")
        break

    else:
        print("Opção inválida. Tente novamente.")
