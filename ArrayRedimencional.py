class ArrayRedi:
    def __init__(self, tam = 4):
        self.tam = tam # tamanho inicial da lsita q é 4
        self.quantVal = 0 # quant de valores inseridos
        self.dados = [None] * tam # 

    def mostrar(self):
        for i in range (self.quantVal):
            print(self.dados[i])

    def inserirFinal(self, elemento):
        if self.quantVal == self.tam:
            self.redimensiona(2* self.tam)

        self.dados[self.quantVal] = elemento
        self.quantVal += 1

    def inserirInicio(self, elemento):
        if self.quantVal == self.tam:
            self.redimensiona(2* self.tam)
        for i in range(self.quantVal, 0, -1): # desloca a lista uma posição para direita para caber um valor na pos 0
            self.dados[i] = self.dados[i - 1]
        self.dados[0] = elemento
        self.quantVal += 1
        print(f"{elemento} foi adicionado ao inicio com sucesso")

    def excluir(self, elemento):
        for i in range(self.quantVal):
            if self.dados[i] == elemento:

                for j in range(i, self.quantVal - 1):  # Desloca os elementos para a esquerda
                    self.dados[j] = self.dados[j + 1]

                self.dados[self.quantVal - 1] = None
                self.quantVal -= 1
                print(f"{elemento} foi removido com sucesso")
                return
        print(f"{elemento} não está na lista")

    def buscar(self, elemento):
        for i in range(self.quantVal):
            if self.dados[i] == elemento:
                print(f"O elemento {elemento} foi encotrado na posição {i}")
                return
        print(f"{elemento} não foi encontrado na lista")


    def redimensiona(self, novoTam):
        novaLista = [None] * novoTam
        for i in range(self.quantVal): # Copia os elementos para a nova lista
            novaLista[i] = self.dados[i]

        self.dados = novaLista # troca a lsta antiga pela nova
        self.tam = novoTam # atualiza a capacidade da lista


array = ArrayRedi()

array.inserirFinal(10)
array.inserirFinal(20)
array.inserirFinal(30)
array.inserirFinal(40)  # Capacidade máxima alcançada
array.inserirFinal(50)  # Redimensiona automaticamente

array.mostrar()

array.inserirInicio(5)
array.mostrar()

array.excluir(20)
array.mostrar()

array.buscar(30)
array.buscar(100)  # Elemento inexistente






