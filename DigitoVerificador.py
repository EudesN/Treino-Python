
def calculoDV(cpf):
    if len(cpf) != 9 or not cpf.isdigit(): 
        return "O CPF precisa possuir 9 digitos"
    
    peso1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    for i in range(9):
        sum(int(cpf[i]) * peso1[i])