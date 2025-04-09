n1 = 0
n2 = 1
num = int(input("informe um número: "))
while(n1 <= num):
    print(n1, end= " ")
    prox = n1 + n2
    n1 = n2 
    n2 = prox 