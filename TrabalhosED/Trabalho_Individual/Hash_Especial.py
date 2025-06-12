class Node:
    def __init__(self, dado):
        self.dado = dado
        self.next = None

class HashTable:
    def __init__(self, cap):
        self.M = cap
        self.N = 0
        self.tab = [None] * cap

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
            aux = aux.next
        raise KeyError(chave)

    def put(self, nome):
        pos = self._hash(nome)
        aux = self.tab[pos]

        while aux:
            if aux.dado == nome:
                print("O nome já está inserido na tabela.")
                return
            aux = aux.next
        
        novo = Node(chave)
        novo.next = self.tab[pos]
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
                    aux = aux.next
                print("None")
        print("---------------------------")
        print(f"Fator de carga: {self.N}/{self.M} = {self.N / self.M:.2f}")


































