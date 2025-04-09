class Fila:
    def __init__(self):
        self.cap = 4                 # capacidade inicial do array
        self.dados = [None] * self.cap  # array inicializado com 4 posições todas com None
        self.inicio = 0                     # índice do primeiro elemento
        self.fim = 0                        # índice onde o próximo será inserido
        self.tam = 0                    # total de elementos na fila

    def enqueue(self, nome):
        if self.tam == self.cap:
            self._redimencionar(self.cap * 2)
        self.dados[self.fim] = nome
        self.fim = (self.fim + 1) % self.cap
        self.tam += 1

    def dequeue(self):
        if self.empty():
            print("A fila está vazia")
            return None
        nome = self.dados[self.inicio]
        self.dados[self.inicio] = None # limpa a posição
        self.inicio = (self.inicio + 1) % self.cap
        self.tam -= 1

        #reduz a capacidade
        if 0 < self.tam <= self.cap // 4 and self.cap > 4:
            self._redimencionar(self.cap // 2)
        return nome
    
    def _redimencionar(self, novaCap):
        novoArray = [None] * novaCap

        for i in range(self.tam):
            novoArray[i] = self.dados[(self.inicio + i) % self.cap]
        self.dados = novoArray
        self.inicio = 0
        self.fim = self.tam
        self.cap = novaCap

    def empty(self):
        return self.tam == 0
    
    def show(self):
        print("\nFila atual: ")
        for i in range(self.tam):
             print(f"- {self.dados[(self.inicio + i) % self.cap]}")
        print(f"Total de pessoas: {self.tam}")

fila = Fila()

while True:
    print("\n=== MENU ===")
    print("1. Enfileirar pessoa")
    print("2. Desenfileirar pessoa")
    print("3. Mostrar fila")
    print("0. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        nome = input("Digite o nome da pessoa: ")
        fila.enqueue(nome)
        print(f"{nome} entrou na fila.")

    elif opcao == '2':
        nome = fila.dequeue()
        if nome:
            print(f"{nome} foi removido da fila.")

    elif opcao == '3':
        fila.show()

    elif opcao == '0':
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
