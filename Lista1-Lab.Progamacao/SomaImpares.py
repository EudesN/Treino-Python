soma = 0
n = int(input("Informe um número: "))
for num in range(1, n + 1):
    if(num % 2 != 0):
        soma += num
print(f"A soma dos valores impares é: {soma}")