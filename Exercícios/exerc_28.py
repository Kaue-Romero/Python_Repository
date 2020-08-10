from random import randint
from time import sleep
N = int(input('Digite um número de 0 até 5: '))
# Gera um número aletório
n = randint(0, 5)
print('-=-' * 50)
print('Processando...')
sleep(2)
print('Pensei no número: {}'.format(n))
print('Você venceu' if N == n else 'Você perdeu')
print('-=-' * 50)
