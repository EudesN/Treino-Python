rota = []

while True:
    print("\nMenu de opções:")
    print("1 - Adicionar novo ponto GPS à rota")
    print("2 - Remover ponto GPS da rota")
    print("3 - Exibir rota atual")
    print("4 - Sair do programa")

    opcao = input("Informe a opção: ")

    if opcao == '1':
        try:
            x = float(input("Informe a coordenada X: "))
            y = float(input("Informe a coordenada Y: "))
            ponto = (x, y)
            rota.append(ponto)
            print(f"Ponto {ponto} adicionado com sucesso!")
        except ValueError:
            print("Coordenadas inválidas")
    
    if opcao == '2':
        if not rota:
            print("Rota vazia")
        else:
            for i, ponto in enumerate(rota):
                print(f"Ponto {i}: {ponto}")

            try:
                indice = int(input("Informe o índice do ponto a ser removido: "))
                if 0 <= indice < len(rota):
                    removido = rota[indice]

                    del rota[indice]
                    print(f"Ponto {removido} removido com sucesso.")
                else:
                    print("Índice fora do intervalo.")
            except ValueError:
                print("Índice inválido")
    
    if opcao == '3':
        if not rota:
            print("A rota está vazia.")
        else:
            print("Rota atual:")
            for i, ponto in enumerate(rota):
                print(f"Ponto{i}: {ponto}")

    elif opcao == '4':
        print("Encerrando programa...")
        break

    else:
        print("Opção inválida")




