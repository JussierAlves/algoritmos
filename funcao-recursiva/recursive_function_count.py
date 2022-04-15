"""
Exemplo de função recursiva que conta os valores de uma lista sem a utilização de laço de repetição.
Infelizmente, não há nenhum benefício em termos de desempenho ao usar funções recursivas em Python, já que laços podem resolver o problema com mais eficiência.

Uma função é recursiva quando ela chama por ela mesma. 
A função recursiva pode ser dividida em duas partes:
1- Caso base;
2- Caso recursivo.
"""

def counter(arr):

    if arr == []:
        return 0  # Caso base.
    else:
        return 1 + counter(arr[1:])  # Caso recursivo.

arr = ['a', 'b', 'c', 'd', 'f']

print(counter(arr))
