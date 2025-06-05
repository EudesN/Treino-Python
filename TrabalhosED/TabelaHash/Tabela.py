class Node:
    def __init__(self, chave, valor):
        self.key = chave
        self.value = valor
        self.prox = None

class HashTable:
    def __init__(self, cap):
        self.M = cap
        self.N = 0
        self.tab = [None] * cap

    def _hash(self, chave):
        chave = chave.lower()
        return hash(chave) % self.M
    
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
        
        # Percorre a lista para verificar se a chave já existe
        aux = self.tab[pos]
        while aux:
            if aux.key == chave:
                aux.value = valor # Atualiza o valor se a chave for encontrada
                return
            aux = aux.prox
        
        # Se a chave não foi encontrada, insere um novo nó no início da lista
        novo = Node(chave, valor)
        novo.prox = self.tab[pos]
        self.tab[pos] = novo
        self.N += 1

    def mostrar(self):
        print("--------Tabela Hash --------")
        for i in range(self.M):
            print(f"{i}: ", end="")
            aux = self.tab[i]
            if aux is None:
                print("Vazio.")
            else:
                while aux:
                    print(f"[{aux.key}: {aux.value}] -> ", end="")
                    aux = aux.prox
                print("None")
        print("---------------------------")

    def maiorValor(self):
        # Inicia 'maior' com None para lidar com qualquer tipo de valor
        maior = None 
        
        # Itera por toda a tabela
        for i in range(self.M):
            aux = self.tab[i]
            # Itera pela lista encadeada em cada posição
            while aux:
                # Se 'maior' ainda for None ou o valor atual for maior
                if maior is None or aux.value > maior:
                    maior = aux.value # Atualiza 'maior' com o novo valor
                aux = aux.prox
        
        return maior