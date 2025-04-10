class Node:
    def __init__(self, cid):
        self.cidade = cid
        self.prox = None

class Lista:
    def __init__(self):
        self.inicio = None
    
    def NovaLista(self):
        novaLista = Lista()
        aux = self.inicio

        while aux != None:
            