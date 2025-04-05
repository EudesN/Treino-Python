class Node:
    def __init__(self, data):
        self.data = data # dado que é empilhado
        self.next = None #  ponteiro para o próximo nó (abaixo dele na pilha)

class Stack:
    def __init__(self): # Contrutor
        self.top = None # o ultimo elemento empilhado(o topo da pilha)
        self.size = 0 # quantos elementos tem na pilha


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
            return node.data
        print("A pilha está vazia")

    def peek(self): # retorna o elemento do topo da pilha sen remover
        if self.size > 0:
            return self.top.data
        print("A pilha está vazia")

    def count(self):
        return self.size
    
    def show(self):
        if(self.size == 0):
            print("A pilha está vazia.")

        r = ""
        pointer = self.top
        while(pointer):
            r += " -> " + str(pointer.data)
            pointer = pointer.next
        return r
    

pilha = Stack()

while True:
    print("\n---------- MENU ----------")
    print("1- Empilhar (push)")
    print("2- Desempilhar (pop)")
    print("3- Mostrar pilha")
    print("4- Mostrar quantidade na pilha")
    print("0- Sair")
    print("--------------------------")


    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = input("Digite um número ou nome para empilhar: ")
        pilha.push(valor)

    elif opcao == "2":
        pilha.pop()

    elif opcao == "3":
        print(pilha.show())

    elif opcao == "4":
        print(pilha.count())

    elif opcao == "0":
        print("Encerrando o programa.")
        break

    else:
        print("Opção inválida! Tente novamente.")




