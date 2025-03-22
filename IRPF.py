



def calculo(salario):
    if salario < 2259.20:
        aliquota = 1
        deducao = 0.00
    elif salario <= 2826.65:
        aliquota = 0.075
        deducao = 158.40
    elif salario <= 3751.05:
        aliquota = 0.15
        deducao = 381.44
    elif salario <= 4664.68:
        aliquota = 0.225
        deducao = 662.77
    else:
        aliquota = 0.275
        deducao = 896.00

    irpf = (salario * aliquota) - deducao
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

tot = calculo(salario)
print(f"O valor do IRPF é: {tot:.2f}")