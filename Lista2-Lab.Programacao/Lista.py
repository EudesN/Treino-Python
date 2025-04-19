alunos = []

while True:
    print("\nMenu de opções:")
    print("1 - Inserir novo aluno")
    print("2 - Buscar aluno")
    print("3 - Exibir alunos em ordem alfabética")
    print("4 - Remover aluno")
    print("5 - Sair")

    opcao = input("Informe a opção: ")

    if opcao == '1':
        nome = str(input("Infome o nome do aluno a ser inserido: ")).strip()
        alunos.append(nome)
        print(f"Aluno {nome} foi inserido com sucesso")
        print(f"Lista atual: {alunos}")
    
    elif opcao == '2':
        nome = str(input("Informe o nome para a busca: ")).strip()
        if nome in alunos:
            print(f"Nome encontrado na lista")
        else:
            print("Nome não encotrado na lista")
    
    elif opcao == '3':
        alunos.sort()
        print(f"A lista em ordem alfabética: {alunos}")

    elif opcao == '4':
        nome = input("Digite o nome do aluno a ser removido: ").strip()
        if nome in alunos:
                alunos.remove(nome)
                print(f"Aluno {nome} removido com sucesso.")
        else:
            print(f"Aluno {nome} não foi encotrado na lista")
        print(f"Lista atual: {alunos}")

    elif opcao == '5':
        print("encerrando programa...")
        break
    else:
        print("Opção inválida. Por favor, digite um número de 1 a 5.")  