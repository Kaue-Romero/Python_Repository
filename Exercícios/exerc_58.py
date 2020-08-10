from random import randint
npc = randint(0, 10)
tentativas = 0
n = int(input('''
O JOGO VAI COMEÇAR!
Escolha um número de 0 até 10: '''))
while n != npc:
    n = int(input('Errou! Tente novamente: '))
    tentativas += 1
print('O computador escolheu o número {}!'.format(npc))
if tentativas == 0:
    print('DÊ PRIMEIRA!')
elif tentativas <= 4:
    print('Você tentou poucas vezes PARABÉNS!')
elif tentativas <= 6:
    print('Cuidado muitas tentativas')
else:
    print('Limite de tentativas excedidas. Tente denovo depois')
print('Você acertou com {} tentativas'.format(tentativas))
