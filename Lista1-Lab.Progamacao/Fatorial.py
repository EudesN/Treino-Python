fatorial = 1
n = int(input("Informe um número: "))
for i in range(n, 0 , -1):
    #print(i)
    fatorial *= i
print(f"O fatorial de {n} é {fatorial}")