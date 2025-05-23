def bubble_sort(lista): 
    n = len(lista)
    for j in range(n - 1 - j): # o 'J'é utilizado como otimização pois os últimos elementos já estão ordenados. Isso evita comparações desnecessárias com elementos já ordenados.
        for i in range(n - 1): # não é necessario percorrer até o ultimo indice pq não há ninguem para comparar depois, então se compara até o penultimo
            if lista[i] > lista[i + 1]: 
                aux = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = aux  # o maior elemento "bolha"  é empurrado para o final da lista

lista_aleatoria = [12, 5, 23, 8, 3, 17, 14, 29, 6, 2, 18, 9, 11, 30, 7, 21, 1, 4, 25, 15]
lista_invertida = [28, 22, 19, 16, 13, 12, 11, 9, 7, 5, 4, 3, 2, 2, 1, 1, 0, 0, -2, -5]
lista_repetidos = [5, 5, 3, 3, 3, 8, 8, 1, 1, 1, 1, 7, 7, 7, 2, 2, 9, 9, 9, 9]



bubble_sort(lista_aleatoria)
bubble_sort(lista_invertida)
bubble_sort(lista_repetidos)

print(f"Lista aleatória ordenada: {lista_aleatoria}")
print(f"Lista invertida ordenada: {lista_invertida}")
print(f"Lista repetida ordenada: {lista_repetidos}")





