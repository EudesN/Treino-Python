def inserirPessoa(dados):
    cpf = int(input("Informe o cpf: "))
    if cpf in dados:
        return

    nome = str(input("Informe seu nome: "))
    endereco = input("Informe seu endereço: ")
    Telefone = input("Informe seu telefone: ")

    dados[cpf] = {'Nome': nome, 'Endereço': endereco, 'Telefone': telefone }








