# implementar uma pilha com duas filas


class Node:
    def __init__(self, data):
        self.data = data
        self.prox = None

class Fila:
    def __init__(self):
        self.first = None
        self.last = None
        
    def PopPilha(self):
        qntd = fila1.quant()
        if qntd == 0:
            print("Fila vazia!")
            return
        elif qntd == 1:
            print(f"{fila1.head.valor} removido")
            fila1.dequeue()
            return
        else:
            aux = fila1.head
            fila2 = Fila()
            for i in range(qntd - 1):
                fila2.enqueue(aux.valor)
                aux = aux.prox
                fila1.dequeue() 
            print(f"{aux.valor} removido!")
            fila1.dequeue()
            fila1.head = fila2.head