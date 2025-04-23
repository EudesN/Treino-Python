pares = []
n = int(input("Informe um número: "))
for num in range(n + 1):
    if(num % 2 == 0):
        pares.append(num)
print(pares)