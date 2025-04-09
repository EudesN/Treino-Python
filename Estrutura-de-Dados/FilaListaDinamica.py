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
    
    def _redimencionar(self, novaCap):
        novoArray = [None] * novaCap