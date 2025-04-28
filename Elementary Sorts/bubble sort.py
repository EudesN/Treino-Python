def bubble_sort(lista):
    n = len(lista)
    for j in range(n - 1):
        for i in range(n - 1): # não é necessario percorrer até o ultimo indice pq não há ninguem para comparar depois, então se compara até o penultimo
            if lista[i] > lista[i + 1]:
                aux = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = aux  




lista = [4, 9, 2, 1, 7, 8]







