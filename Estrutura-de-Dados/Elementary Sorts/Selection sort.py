def selection_sort(lista):
    min_index = 0
    for j in range(len(lista) - 1): # controla a lista que precisa ser analizada a cada interação. E '-1' pq o ultimo elemento já vai estar ordenado ao final
        min_index = j # o inidice minimo é inciado em j pq o menor valor sempre sera alocado na posição j + 1
        for i in range(j, len(lista)):
            if lista[i] < lista[min_index]: # encontrar o menor valor
                min_index = i # armazena o menor valor, prcurando dentro dos valores q ainda não estão ordenados
        if lista[j] > lista[min_index]: # realiza a troca do menor valor para a prosição indicada por j
            aux = lista[j]
            lista[j] = lista[min_index]
            lista[min_index] = aux


lista_aleatoria = [12, 5, 23, 8, 3, 17, 14, 29, 6, 2, 18, 9, 11, 30, 7, 21, 1, 4, 25, 15]
lista_invertida = [28, 22, 19, 16, 13, 12, 11, 9, 7, 5, 4, 3, 2, 2, 1, 1, 0, 0, -2, -5]
lista_repetidos = [5, 5, 3, 3, 3, 8, 8, 1, 1, 1, 1, 7, 7, 7, 2, 2, 9, 9, 9, 9]

selection_sort(lista_aleatoria)
selection_sort(lista_invertida)
selection_sort(lista_repetidos)




print(f"Lista aleatória ordenada: {lista_aleatoria}")
print(f"Lista invertida ordenada: {lista_invertida}")
print(f"Lista repetida ordenada: {lista_repetidos}")