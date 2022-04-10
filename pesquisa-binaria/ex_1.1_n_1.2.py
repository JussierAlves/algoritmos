"""
Suponha que você tenha uma lista com 128 nomes e esteja fazendo uma
pesquisa binária. Qual seria o número máximo de etapas que você levaria
para encontrar o nome desejado?
"""

num = 128
count = 0

def counter(num, count):
    while num > 1:
        num = num / 2
        count += 1
    
    print(count)

counter(num, count)


"""
Suponha que você duplique o tamanho da lista. Qual seria o número
máximo de etapas agora?
"""

counter(256, count)

