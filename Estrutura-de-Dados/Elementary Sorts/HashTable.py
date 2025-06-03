class Node:
    def __init__(self, chave, valor):
        self.key = chave #identifica o dado por uma chave
        self.value = valor # dado armazenado
        self.prox = None # referencia para o proximo

class HashTable:
    def __init__(self, cap): # Inicializa a tabela com um tamanho fixo
        self.M = cap  # Capacidade da tabela
        self.N = 0 # Número de chaves na tabela
        self.tab = [None] * cap # Cria uma lista de tamanho 'cap', onde cada posição é None. Esta é a tabela principal.

    def _hash(self, chave): # função hash ou função de dispersão (transforma a chave em um indice)
        return hash(chave) % self.M # Usa a função interna do Python para converter a chave em um número inteiro grande
    
    def get(self,chave):
        pos = self._hash(chave) # qual índice procurar
        aux = self.tab[pos]
        while aux: # enquanto existir um Node na lista encadeada
            if aux.key == chave:
                return aux.value
            aux = aux.prox
        raise KeyError(chave) # chave não encontrada

    def put(self, chave, valor):
        pos = self._hash(chave) # calcula o indice 
        if self.tab[pos] is None: # se a posição for vazia cria um novo nó com chave e valor
            self.tab[pos] = Node(chave, valor)
        else: # caso haja colisão : já existe pelo menos um Node ocupando esse índice
            aux = self.tab[pos]
            while aux: # percorre a lista de nós que já existe naquela posição
                if aux.key == chave:
                    aux.value = valor # Caso a chave já exista, simplesmente atualiza o valor
                    return
                aux = aux.prox
            # Caso não encontre a chave após percorrer toda lista, insiro no início
            novo = Node(chave, valor)
            novo.prox = self.tab[pos]
            self.tab[pos] = novo
        
        self.N += 1 # atualiza o contador total de pares inseridos








