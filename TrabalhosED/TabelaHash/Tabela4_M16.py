# Para a questão 4 da lista

import matplotlib.pyplot as plt

class Node:
    def __init__(self, chave, valor):
        self.key = chave
        self.value = valor
        self.prox = None

class HashTable:
    def __init__(self, M):
        self.M = M
        self.N = 0
        self.tab = [None] * M

    def _hash(self, chave):
        chave = chave.lower()
        h = 0
        for c in chave:
            h = (h * 31 + ord(c)) % self.M
        return h
    

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

    def contColisoes(self):
        colisoes = []
        for i in range(self.M):
            cont = 0
            aux = self.tab[i]
            while aux:
                cont += 1
                aux = aux.prox
            colisoes.append(cont)
        return colisoes

tb = HashTable(16)

nomes = []

try:
    with open("alunosED_2025.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            nome = linha.strip()
            if nome:  
                nomes.append(nome)
except FileNotFoundError:
    print("ERROR: Arquivo 'alunosED2025.txt' não encontrado. Verifique o nome e o caminho.")
    nomes = []  


for nome in nomes:
    tb.put(nome, 1)

colisoes = tb.contColisoes()

letras = [f'{i}' for i in range(tb.M)]

# Gera o histograma
plt.figure(figsize=(12, 5))
plt.bar(letras, colisoes)
plt.xlabel('Letra inicial (minúscula)')
plt.ylabel('Quantidade de nomes')
plt.title('Distribuição dos nomes dos alunos na Tabela Hash  (M = 16)', pad=20)

plt.text(0.5, 1.02, 'Utilizando a função Hash da linguagem Python',
         ha='center', va='center', transform=plt.gca().transAxes,
         fontsize=10, color='black')

plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.show()

print("Colisões (quantidade de nomes em cada índice):")
print(colisoes)

if colisoes:
    max_col = max(colisoes)
    min_col = min(colisoes)

    letras_max = [letras[i] for i, c in enumerate(colisoes) if c == max_col]
    letras_min = [letras[i] for i, c in enumerate(colisoes) if c == min_col]

    print(f"\nLetras com mais colisões ({max_col} nomes): {letras_max}")
    print(f"Letras com menos colisões ({min_col} nomes): {letras_min}")
else:
    print("Nenhum nome foi inserido, portanto não há colisões para mostrar.")




