class Node:
    def __init__(self, chave, valor):
        self.key = chave
        self.value = valor
        self.next = None

class HashTable:
    def __init__(self, cap):
        self.M = cap
        self.N = 0
        self.tab = cap * [None]


def _hash(self, chave):
    chave = chave.lower()
    soma = 0
    for c in chave:
        soma += ord(c)
    return hash(soma) % self.M


class Node:
    def __init__(self, chave, valor):
        self.key = chave
        self.value = valor
        self.next = None

class HashTable:
    def __init__(self, cap):
        self.M = cap
        self.N = 0
        self.tab = cap * [None]

    def _hash(self, chave):
        chave = chave.lower()
        soma = 0
        for c in chave:
            soma += ord(c)
        return hash(soma) % self.M

    def get(self, chave):
        pos = self._hash(chave)
        aux = self.tab[pos]
        while aux:
            if aux.key == chave:
                return aux.value
            aux = aux.prox
        raise KeyError(chave)

    def put(self, chave, valor):
        pos = self._hash(chave)
        
        aux = self.tab[pos]
        while aux:
            if aux.key == chave:
                aux.value = valor 
                return
            aux = aux.prox
        
        novo = Node(chave, valor)
        novo.prox = self.tab[pos]
        self.tab[pos] = novo
        self.N += 1


































