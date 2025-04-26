def inserirPessoa(dados):
    cpf = int(input("Informe o cpf: "))
    if cpf in dados:
        return

    nome = str(input("Informe seu nome: "))
    endereco = input("Informe seu endereço: ")
    telefone = input("Informe seu telefone: ").split(",")

    dados[cpf] = {'Nome': nome, 'Endereco': endereco, 'Telefones': telefone }

    print("pessoas cadastrada com sucesso")

def listarPessoas(dados):
    if not dados:
        print("Nenhuma pessoa foi cadastrada")
        return
    for cpf, info in dados.items():
        print(f"CPF: {cpf}")
        print(f"Nome: {info['Nome']}")
        print(f"Endereço: {info['Endereco']}")
        print(f"Telefones: {', '.join(info['Telefones'])}")
        print("-" * 30)

def buscarPorCpf(dados):
    if not dados:
        print("Nenhuma pessoa foi cadastrada")
        return
    cpf = int(input("Informe o cpf para a busca: "))
    pessoa = dados.get(cpf)

    if pessoa:
        print(f"Nome: {pessoa['Nome']}")
        print(f"Endereço: {pessoa['Endereco']}")
        print(f"Telefones: {', '.join(pessoa['Telefones'])}")
        return
    else:
        print("Pessoa não encontrada")

def buscarPorTelefone(dados):
    telBusca = input("Informe o telefone para a busca: ")
    for cpf, pessoa in dados.items():
        if telBusca in pessoa['Telefones']:
            print(f"Nome: {pessoa['Nome']}")
            print(f"Endereço: {pessoa['Endereco']}")
            print(f"Telefones: {', '.join(pessoa['Telefones'])}")
            return
    print("Telefone não foi cadastrado")

def removerPorCpf(dados):
    cpf = int(input("Informe o cpf para a busca: "))
    if cpf in dados:
        del dados[cpf]
        print("Pessoa removida com sucesso.\n")
    else:
        print("CPF não encontrado")

def menu():
    pessoas = {}

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
            inserirPessoa(pessoas)
        
        elif opcao == '2':
            listarPessoas(pessoas)

        elif opcao == '3':
            buscarPorCpf(pessoas)

        elif opcao == '4':
            buscarPorTelefone(pessoas)
        
        elif opcao == '5':
            removerPorCpf(pessoas)
        
        elif opcao == '6':
            print("Encerrando programa...")
            break

        else:
            print("Opcão Inválida")

menu()