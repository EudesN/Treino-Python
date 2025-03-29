class ArrayRedi:
    def __init__(self, tam = 4):
        self.tam = tam
        self.quantVal = 0
        self.dados = [None] * tam

def mostrar(self):
    lista = []
    for i in range (self.quantVal):
        print(i)

def inserirFinal(self, elemento):
    if self.quantVal == self.tam:
        self.redimenciona(2* self.tam)

    self.dados[self.quantVal] = elemento
    self.quantVal += 1

def inserirInicio(self, elemento):
    if self.quantVal == self.tam:
        self.redimenciona(2* self.tam)
        # desloca a lista uma posição para direita para caber um valor na pos 0
        for i in range(self.quantVal, 0, -1): 
            self.dados[i] = self.dados[i - 1]
        self.dados[0] = elemento
        self.quantVal += 1