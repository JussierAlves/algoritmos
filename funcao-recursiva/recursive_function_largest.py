"""
Exemplo de função recursiva que encontra o maior valor em um índice de uma lista sem a utilização de laço de repetição.
Infelizmente, não há nenhum benefício em termos de desempenho ao usar funções recursivas em Python, já que laços podem resolver o problema com mais eficiência.

Uma função é recursiva quando ela chama por ela mesma. 
A função recursiva pode ser dividida em duas partes:
1- Caso base;
2- Caso recursivo.
"""

def largestValue(arr):

    if len(arr) == 1:
        return arr[0]  # Caso base.
    else:
        tail = largestValue(arr[1:])
        return tail if tail > arr[0] else arr[0]  # Caso recursivo.


arr = [2,5,9,3,4]
print(largestValue(arr))
