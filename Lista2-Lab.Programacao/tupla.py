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
        except:
            print("Coordenadas inválidas")
    
    if opcao == '2':
        if not rota:
            print("Rota vazia")


