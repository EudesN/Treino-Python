class Fila:
    def __init__(self):
        self.cap = 4                 # capacidade inicial do array
        self.dados = [None] * self.cap  # array inicializado com 4 posições todas com None
        self.inicio = 0                     # índice do primeiro elemento
        self.fim = 0                        # índice onde o próximo será inserido
        self.tam = 0                    # total de elementos na fila    

    def enqueue(self, nome):
        if self.tam == self.cap: # antes de inserir verifica se o array está cheio 
            self._redimencionar(self.cap * 2) # se sim, é necessario chamar a função redimencionar
        self.dados[self.fim] = nome # insere o nome na posição 'fim'
        self.fim = (self.fim + 1) % self.cap # garante que quando chegar ao final do array o índice volte para o início (é circular).
        self.tam += 1

    def dequeue(self): # remove o nome do inicio da fila e retorna esse nome
        if self.empty():
            print("A fila está vazia")
            return None
        
        nome = self.dados[self.inicio] # nome é igual ao primeiro elemento da fila
        self.dados[self.inicio] = None # faz a limpeza
        self.inicio = (self.inicio + 1) % self.cap  # move o início
        self.tam -= 1

        #reduz a capacidade
        if 0 < self.tam <= self.cap // 4 and self.cap > 4:
            self._redimencionar(self.cap // 2)
        return nome
    
    def _redimencionar(self, novaCap): # ajustar o tamanho do array
        novoArray = [None] * novaCap #novo array de acordo com a capacidade necessaria  

        for i in range(self.tam): # os dados do array antigo são copiados no novo
            novoArray[i] = self.dados[(self.inicio + i) % self.cap]
        # atualiza os ponteiros da fila para funcionar no novo array
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
