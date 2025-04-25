def inserirPessoa(dados):
    cpf = int(input("Informe o cpf: "))
    if cpf in dados:
        return

    nome = str(input("Informe seu nome: "))
    endereco = input("Informe seu endereço: ")
    telefone = input("Informe seu telefone: ")

    dados[cpf] = {'Nome': nome, 'Endereço': endereco, 'Telefone': telefone }

    print("pessoas cadastrada com sucesso")

# def listarPessoas(dados):

def menu():
    pessoas = {}

while True:
    

    print("1. Inserir pessoa")
    print("2. Listar pessoas cadastradas")
    print(" 3. Buscar pessoa por CPF")
    print("4. Buscar pessoa por Telefone")
    print(" 5. Remover pessoa por CPF")
    print(" 6. SAIR")

    opcao = input("Informe a opção desejada: ")

    if opcao == '1':
        inserirPessoa(pessoas)
    

    if opcao == '6':
        print("Encerrando programa...")
        break

    else:
        print("Opcão Inválida")

menu()