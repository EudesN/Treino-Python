
def inserirPessoa():
    cpf = input("Informe o cpf: ")
    nome = input("Informe seu nome: ")
    endereco = input("Informe seu endereço: ")
    telefone = input("Informe seu telefone: ")
    with open('arquivos.txt', 'a') as arquivo:
        arquivo.write(f"{cpf},{nome},{endereco},{telefone}\n")

def listarPessoas():
    with open('arquivos.txt', 'r') as arquivo:
        listagem = arquivo.readlines()
        for linha in listagem:
            dados = linha.strip().split(',')
            if len(dados) >= 4:
                print(f"Nome: {dados[1]} | CPF: {dados[0]}  | Endereço: {dados[2]} | Telefone: {dados[3]}")
            else:
                print("Linha de informações incompleta ou inválida", linha.strip())

def BuscarPorCPF():
    cpf = input("Informe o cpf para a busca: ")
    with open('arquivos.txt', 'r') as arquivo:
        listagem = arquivo.readlines()
        for linha in listagem:
            dados = linha.strip().split(',')
            if(dados[0] == cpf):
                print(f"Nome: {dados[1]} | CPF: {dados[0]}  | Endereço: {dados[2]} | Telefone: {dados[3]}")
                return
    print("O CPF não foi encotrado nos arquivos")

def BuscarPorTelefone():
    telefone = input("Informe o telefone para a busca: ")
    with open('arquivos.txt', 'r') as arquivo:
        listagem = arquivo.readlines()
        for linha in listagem:
            dados = linha.strip().split(',')
            if(dados[3] == telefone):
                print(f"Nome: {dados[1]} | CPF: {dados[0]}  | Endereço: {dados[2]} | Telefone: {dados[3]}")
                return
    print("O telefone não foi encotrado nos arquivos")

def removerPorCpf():
    cpf = input("Informe o cpf para a busca: ")
    with open('arquivos.txt', 'r') as arquivo:
        listagem = arquivo.readlines()
        for linha in listagem:
            dados = linha.strip().split(',')
            if(dados[0] == cpf):
                print(f"Nome: {dados[1]} | CPF: {dados[0]}  | Endereço: {dados[2]} | Telefone: {dados[3]}")
                return
    print("O CPF não foi encotrado nos arquivos")



while True:

    print("-" * 30)
    print("1. Inserir pessoa")
    print("2. Listar pessoas cadastradas")
    print("3. Buscar pessoa por CPF")
    print("4. Buscar pessoa por Telefone")
    print("5. Remover pessoa por CPF")
    print("6. SAIR")
    print("-" * 30)

    opcao = input("Informe a opção desejada: ")

    if opcao == '1':
        inserirPessoa()
    
    elif opcao == '2':
        listarPessoas()

    elif opcao == '3':
        buscarPorCpf()

    elif opcao == '4':
        buscarPorTelefone()
    
    elif opcao == '5':
        removerPorCpf()
    
    elif opcao == '6':
        print("Encerrando programa...")
        break

    else:
        print("Opcão Inválida")
