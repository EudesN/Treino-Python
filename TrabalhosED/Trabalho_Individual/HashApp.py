from Hash_Especial import HashTable


if __name__ == "__main__":
    # Solicita ao usuário o valor de M (capacidade da tabela hash)
    while True:
        try:
            M = int(input("Informe a capacidade da tabela hash (valor de M): "))
            if M <= 0:
                print("Digite um número maior que zero.")
            else:
                break
        except ValueError:
            print("Digite um número inteiro válido.")

    tb = HashTable(M)  # Agora M é informado pelo usuário
    while True:
        print("\n--- MENU ---")
        print("1 - Incluir nome")
        print("2 - Buscar nome")
        print("3 - Mostrar tabela")
        print("0 - Sair")

        try:
            op = int(input("Informe sua opção: "))
        except ValueError:
            print("Digite um número válido.")
            continue

        match op:
            case 1: 
                chave = input("Nome? ")
                valor = input("Valor? ")  # Ex: idade, telefone, etc.
                tb.put(chave, valor)
                print("Nome inserido com sucesso!")

            case 2: 
                chave = input("Nome? ")
                try:
                    print(f"Valor encontrado: {tb.get(chave)}")
                except KeyError:
                    print("Nome não encontrado.")

            case 3:
                tb.mostrar()

            case 0:
                print("Encerrando...")
                break

            case _:
                print("Opção inválida.")
