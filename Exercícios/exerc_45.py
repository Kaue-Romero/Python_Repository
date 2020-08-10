from random import randint
from time import sleep
n2 = randint(1, 3)
n = int(input('''
Suas opções:
[ 1 ] PEDRA
[ 2 ] PAPEL 
[ 3 ] TESOURA
Qual é a sua jogada? '''))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
if n == 1:
    print('Jogador escolheu PEDRA')
elif n == 2:
    print('Jogador escolheu PAPEL')
elif n == 3:
    print('Jogador escolheu TESOURA')
else:
    print('Jogada inválida!')
if n2 == 1:
    print('Computador escolheu PEDRA')
elif n2 == 2:
    print('Computador escolheu PAPEL')
else:
    print('Computador escolheu TESOURA')
if n == n2:
    print('-=-' * 11)
    print('EMPATE')
    print('-=-' * 11)
elif n == 1 and n2 == 2:
    print('-=-' * 11)
    print('Computador GANHOU!')
    print('-=-' * 11)
elif n == 1 and n2 == 3:
    print('-=-' * 11)
    print('Jogador GANHOU!')
    print('-=-' * 11)
elif n == 2 and n2 == 3:
    print('-=-' * 11)
    print('Computador GANHOU!')
    print('-=-' * 11)
elif n == 3 and n2 == 1:
    print('-=-' * 11)
    print('Computador GANHOU!')
    print('-=-' * 11)
elif n == 2 and n2 == 1:
    print('-=-' * 11)
    print('Jogador GANHOU!')
    print('-=-' * 11)
elif n == 3 and n2 == 2:
    print('-=-' * 11)
    print('Jogador GANHOU!')
    print('-=-' * 11)


