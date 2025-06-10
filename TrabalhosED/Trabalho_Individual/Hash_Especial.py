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
    return hash(chave) % self.M



















