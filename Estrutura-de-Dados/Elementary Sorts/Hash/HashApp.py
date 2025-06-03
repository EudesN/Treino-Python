import HashTable

class HashApp:
    if __name__ == "__main__":
        tb = HashTable(11)

        while True:
            op = int(input("1.Incluir\n2.Buscar\n3.Mostrar\n4.Sair\n"))
            
            match op:
                case 1: #Incluir item <chave, valor>
                    chave = input("Nome? ")
                    valor = int(input("Valor? "))
                    tb.put(chave, valor)
                
                case 2: #Buscar um item pela <chave>
                    chave = input("Nome? ")
                    print(tb.get(chave))

                case 3: #Mostrar todos os elementos da Hash
                    tb.mostrar()
                
                case 4:
                    break