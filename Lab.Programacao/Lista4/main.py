
def inserirPessoas():
    cpf = int(input("Informe o cpf: "))
    nome = str(input("Informe seu nome: "))
    endereco = input("Informe seu endereço: ")
    telefone = input("Informe seu telefone: ").split(",")
    with open('arquivos.txt', 'w') as arquivo:
        arquivo.write(cpf)
        arquivo.write(nome)
        arquivo.write(endereco)
        arquivo.write(telefone)

def listarPessoas():
    with open('arquivos.txt', 'r') as arquivo:
        lista = arquivo.readline()
        print(lista)




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
