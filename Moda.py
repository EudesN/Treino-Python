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

print(contador)
print(fMax)


