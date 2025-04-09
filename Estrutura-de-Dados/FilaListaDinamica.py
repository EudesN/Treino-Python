class Fila:
    def __init__(self):
        self.cap = 4                 # capacidade inicial do array
        self.dados = [None] * self.cap  # array com valores None
        self.inicio = 0                     # índice do primeiro elemento
        self.fim = 0                        # índice onde o próximo será inserido
        self.tam = 0                    # total de elementos na fila

    def enqueue(self, nome):
        if self.tam == self.cap:
            self._redimencionar(self.cap * 2)
        self.dados[self.fim] = None
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
            self._redimencionar(self.cap / 2)
    
    def _redimencionar(self, novaCap):
        novoArray = [None] * novaCap
    
    def empty(self):
        return len(self) == 0