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

    def mostrar(self):
        print("--------Tabela Hash --------")
        for i in range(self.M):
            print(f"{i}: ", end="")
            aux = self.tab[i]
            if(aux is None):
                print("Vazio.")
            else:
                while aux:
                    print(f"[{aux.key}: {aux.value}] -> ", end="")
                    aux = aux.prox
                print("None")
        print("---------------------------")

    def maiorValor(self):
        maior = 0
        for i in range(self.M):
            aux = self.tab[i]
            while aux:
                if aux is None:
                    maior = aux.value
            else:
                if aux.value > maior:
                    maior = aux
                aux = aux.prox
        return maior

































