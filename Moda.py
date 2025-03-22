def calcular_moda(valores):
    contagem = {}
    for valor in valores:
        if valor in contagem:
            contagem[valor] += 1
        else:
            contagem[valor] = 1

    frequencia_maxima = max(contagem.values())

    modas = [num for num, freq in contagem.items() if freq == frequencia_maxima]

valores = []

resp = 'sim'
while(resp != 'NÃO' or 'NAO' or 'N'):
    n = int(input("Informe o valor: ")).upper().split()
    valores.apend(n);
    resp = int("Deseja adicionar mais números[sim/não]? ")

tipo_moda, modas = calcular_moda(valores)

if modas:
    print(f"Valor(es) da moda: {', '.join(map(str, modas))}")
