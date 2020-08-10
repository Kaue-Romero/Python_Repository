from random import randint
from time import sleep


def maior(* num):
    cont = maior2 = 0
    print('\nAnalisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='')
        if cont == 0:
            maior2 = valor
        else:
            if valor > maior2:
                maior2 = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior2}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 9)
maior(1, 2)
maior(6)
maior()
