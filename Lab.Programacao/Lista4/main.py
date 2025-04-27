
def inserirPessoa():
    cpf = input("Informe o cpf: ").strip()
    nome = input("Informe seu nome: ").strip()
    endereco = input("Informe seu endereço: ").strip()

    telefones = []
    while True:
        telefone = input("Informe um telefone (deixe em branco para parar): ").strip()
        if telefone:
            telefones.append(''.join(filter(str.isdigit, telefone))) #vai tirar quanquer caractere q não seja um digito
        elif not telefones:
            print("É necessário informar um telefone pelo menos")
        else:
            break


    with open('arquivos.txt', 'a') as arquivo:
        arquivo.write(f"{cpf},{nome},{endereco},{';'.join(telefones)}\n")
        print("Pessoa cadastrada com sucesso")

def listarPessoas():
    try:
        with open('arquivos.txt', 'r') as arquivo:
            listagem = arquivo.readlines()
            for linha in listagem:
                dados = linha.strip().split(',')
                if len(dados) >= 4:
                    print(f"Nome: {dados[1]} | CPF: {dados[0]}  | Endereço: {dados[2]} | Telefone: {dados[3]}")
                else:
                    print("Linha de informações incompleta ou inválida", linha.strip())
    except FileNotFoundError:
        print("Nenhuma pessoa cadastrada")

def buscarPorCpf():
    cpf = input("Informe o cpf para a busca: ").strip()
    try:
        with open('arquivos.txt', 'r') as arquivo:
            existe = False
            for linha in arquivo:
                dados = linha.strip().split(',')
                if dados[0] == cpf:
                    telefones = dados[3].split(';')
                    print(f"Nome: {dados[1]} | CPF: {dados[0]}  | Endereço: {dados[2]} | Telefone: {','.join(telefones)}")
                    existe = True
                    break
            if not existe:
                print("O CPF não foi encotrado nos arquivos")
    except FileNotFoundError:
        print("Nenhuma pessoa cadastrada ainda.")


def buscarPorTelefone():
    telefone = input("Informe o telefone para a busca: ").strip()
    try:
        with open('arquivos.txt', 'r') as arquivo:
            existe = False
            for linha in arquivo:
                dados = linha.strip().split(',')
                if len(dados) >= 4:
                    if telefone in dados[3].split(';'):
                        telefones = dados[3].split(';')
                        print(f"Nome: {dados[1]} | CPF: {dados[0]} | Endereço: {dados[2]} | Telefones: {','.join(telefones)}")
                        existe = True
                        break
                else:
                    continue
            if not existe:
                print("Telefone não encontrado nos arquivos.")

    except FileNotFoundError:   
        print("Nenhuma pessoa cadastrada ainda.")


def removerPorCpf():
    cpf = input("Informe o cpf para a busca: ").strip()
    existe = False
    
    try:
        with open('arquivos.txt', 'r') as arquivo:
            listagem = arquivo.readlines()
            linhasNovas = []

            for linha in listagem:
                if not linha.startswith(cpf + ','):
                    linhasNovas.append(linha)
                else:
                    existe = True

        if existe:
            with open('arquivos.txt', 'w') as arquivo:
                arquivo.writelines(linhasNovas)
                print("Pessoa removida com sucesso")
        else:
            print("O CPF não foi encontrado nos arquivos")

    except FileNotFoundError:
        print("Nenhum dado foi cadastrado")


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
