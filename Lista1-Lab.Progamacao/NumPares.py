pares = []
n = int(input("Informe um número: "))
for num in range(n):
    if(n % 2 == 0):
        pares.append(num)
print(pares)