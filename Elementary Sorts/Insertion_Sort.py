def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n): # O primeiro elemento é ignorado  pois uma lista com um unico elemento já está ordenada
        chave = lista[i]
        j = i - 1 # representa a parcela da lista que já está ordenada
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave # mais 1 pq vc sempre vai terminar uma posição antes de onde deveria inserir


lista_aleatoria = [12, 5, 23, 8, 3, 17, 14, 29, 6, 2, 18, 9, 11, 30, 7, 21, 1, 4, 25, 15]
lista_invertida = [28, 22, 19, 16, 13, 12, 11, 9, 7, 5, 4, 3, 2, 2, 1, 1, 0, 0, -2, -5]
lista_repetidos = [5, 5, 3, 3, 3, 8, 8, 1, 1, 1, 1, 7, 7, 7, 2, 2, 9, 9, 9, 9]

insertion_sort(lista_aleatoria)
insertion_sort(lista_invertida)
insertion_sort(lista_repetidos)




print(f"Lista aleatória ordenada: {lista_aleatoria}")
print(f"Lista invertida ordenada: {lista_invertida}")
print(f"Lista repetida ordenada: {lista_repetidos}")







