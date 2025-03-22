
def calculoDV(cpf):
    if len(cpf) != 9 or not cpf.isdigit(): 
        return "O CPF precisa possuir 9 digitos"
    
    peso1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    soma1 = sum(int(cpf[i]) * peso1[i] for i in range(9))
    res = soma1 % 11

    if res < 2:
        dv1 = 0
    else:
        dv1 = 11 - res
    
    peso2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    soma2 = sum(int(cpf[i]) * peso2[i] for i in range(9)) + dv1 * 2
    res2 = soma2 % 11

    if res2 < 2:
        dv2 = 0
    else:
        dv2= 11 - res2

    print(f"{cpf[:3]} {cpf[3:6]} - {dv1} {dv2}")

cpf = input("Digite os 9 primeiros dígitos do CPF (sem pontos ou hífen): ")
calculoDV(cpf)

