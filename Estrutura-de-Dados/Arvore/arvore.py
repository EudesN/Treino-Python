class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    
class Bst:
    def __init__(self):
        self.root = None
    
    def put(self, key, auxRoot):
        if auxRoot is None:
            auxRoot = Node
        elif auxRoot == key:
            raise KeyError("chave já existe.")
        elif auxRoot < key:
            self.put(key, auxRoot.right)
        elif auxRoot > key:
            self.put(key, auxRoot.right)
        return auxRoot

    def inOrder(self, auxRoot):
        if auxRoot:
            self.inOrder(auxRoot.left)
            print(auxRoot.key)
            self.inOrder(auxRoot.right)
    
    def preOrder(self, auxRoot):

if __name__ == "__main__":
    