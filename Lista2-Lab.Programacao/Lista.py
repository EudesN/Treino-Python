Lista = []

while True:
    print("\nMenu de opções:")
    print("1 - Inserir novo aluno")
    print("2 - Buscar aluno")
    print("3 - Exibir alunos em ordem alfabética")
    print("4 - Remover aluno")
    print("0 - Sair")

    opcao = input("Informe a opção: ")

    if opcao == '1':
        nome = str(input("Infome o nome do aluno a ser inserido: "))
        Lista.append(nome)
    
    elif opcao == '2':
        nome = str(input("Informe o nome para a busca: "))

        for n in Lista:
            if Lista[n] == nome:
                print(f"Nome encontrado na lista na posição {n}.")
            else:
                print("Nome não encotrado na lista")
    
    elif opcao == '3':
        Lista.sort()
        print(f"A lista em ordem alfabética: {Lista}")

    elif opcao == '4':
        nome = input("Digite o nome do aluno a ser removido: ").strip()
        for n in Lista:
            if Lista[n] == nome:
                Lista.remove(nome)
                print(f"Aluno {nome} removido com sucesso.")
            else:
                print(f"Aluno {nome} não foi encotrado na lista")
        

    elif opcao == '0':
        print("encerrando programa...")
        break
    else:
        print("Opção inválida. Por favor, digite um número de 1 a 5.")  