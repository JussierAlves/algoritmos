"""
Algoritmo de ordenação por seleção com tempo de execução O(n^2) ou O(n * n).
"""

# Encontra o menor valor do vetor


def findLower(arr):

    lowerValue = arr[0]
    lowerIndex = 0

    for i in range(1, len(arr)):
        if arr[i] < lowerValue:
            lowerValue = arr[i]
            lowerIndex = i
    return lowerIndex


# Armazena os valores em ordem crescente em um novo vetor 

def sortingSelection(arr):

    newArr = []
    for i in range(len(arr)):
        lowerValue = findLower(arr)
        newArr.append(arr.pop(lowerValue))
    return newArr

arr = [50,12,5,9,7,11]


print(sortingSelection(arr))