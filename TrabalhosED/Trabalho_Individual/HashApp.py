from Hash_Especial import HashTable


class HashApp:
    if __name__ == "__main__":
        tb = HashTable(11)

        while True:
            print("1 - Incluir")
            print("2- Buscar")
            print("3- Mostrar")
            print("0- Sair")

            op = int(input("informe sua opção: "))

            match op:
                case 1: #Incluir item <chave, valor>
                    chave = input("Nome? ")
                    tb.put(chave, valor)
                
                case 2: #Buscar um item pela <chave>
                    chave = input("Nome? ")
                    print(tb.get(chave))

                case 3: #Mostrar todos os elementos da Hash
                    tb.mostrar()

                case 0:
                    break