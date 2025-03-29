class No:
    def __init__(self, dado):
        self.dado = dado        # O valor armazenado no nó
        self.proximo = None     # Referência para o próximo nó

class ListaEncadeada:
    def __init__(self):
        self.pElemento  = None