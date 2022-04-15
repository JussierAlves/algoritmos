"""
Exemplo de função recursiva que soma os valores de uma lista sem a utilização de laço de repetição.
Infelizmente, não há nenhum benefício em termos de desempenho ao usar funções recursivas em Python, já que laços podem resolver o problema com mais eficiência.

Uma função é recursiva quando ela chama por ela mesma. 
A função recursiva pode ser dividida em duas partes:
1- Caso base;
2- Caso recursivo.
"""


def sum(arr):

    if len(arr) == 1:
        return arr[0]  # Caso base.
    else:
        return arr[0] + sum(arr[1:])  # Caso recursivo.


arr = [3, 5, 1]

print(sum(arr))
