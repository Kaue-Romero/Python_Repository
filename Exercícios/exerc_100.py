from random import randint
lista = []


def sorteia():
    for c in range(0, 5):
        lista.append(randint(0, 9))
    print(f'Sorteando 5 valores da lista: {lista} Pronto!')


def par():
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {lista}, temos {soma}')


(sorteia(), par())
