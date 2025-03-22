valores = []
contador = {}

x = int(input("Informe quantos números deseja adicinar: "))

while(len(valores) < x):
    num = int(input("Informe o número: "))
    valores.append(num)

for n in valores:
    if n in contador.keys():
        contador[n] += 1
    else:
        contador[n] = 1

fMax = max(contador.values())

modas = []

for k, freq in contador.items():
    if freq == fMax:
        modas.append(k)

print("A moda(s) são " + modas)


