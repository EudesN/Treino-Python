def calculo(salario):
    if salario < 2259.20:
        aliq = 0
        dedut = 0.00
    elif salario >= 2259.21 and salario <= 2826.65:
        aliq = 0.075
        dedut = 158.40
    elif salario >= 2826.66 and salario <= 3751.05:
        aliq = 0.15
        dedut = 381.44
    elif salario >= 3751.06 and salario <= 4664.68:
        aliq = 0.225
        dedut = 662.77
    else:
        aliq = 0.275
        dedut = 896.00

    irpf = (salario * aliq) - dedut
    return(irpf)

while True:
    try:
        salario = float(input("Informe o salário base: "))
        if salario <= 0:
            print("Erro: Valor inválido! O salário deve ser maior que zero.")
        else:
            break
    except:
        print("Erro: Entrada inválida! Digite um valor numérico válido.")

print(f"O valor do IRPF é: {calculo(salario):.2f}")