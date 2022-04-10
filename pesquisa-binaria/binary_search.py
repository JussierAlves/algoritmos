def binary_search(lst, item):
    """
    Pesquisa um item em uma lista ordenada, dividindo pela metade
    e redimensionando o vetor até que reste apenas o item 
    procurado.

    Caso o item não esteha na lista, o retorno sera None. 
    """


    low = 0
    high = len(lst) -1
    while low <= high:
        mid = int((low + high) / 2)
        guessed_number = lst[mid]

        if item == guessed_number:
            return mid
        if item > guessed_number:
            low = mid + 1
        else:
            high = mid-1
    
    return None

lst = [1,3,3,4,5,5,9,11,23]

print(binary_search(lst, 10)) # Retorna None
print(binary_search(lst, 3)) # Retorna 1