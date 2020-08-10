from random import randint
v = 0
while True:
    print('VAMOS JOGAR PAR OU ÍMPAR')
    n = int(input('Digite um valor: '))
    npc = randint(0, 100)
    soma = n + npc
    par = soma % 2 == 0
    escolha = str(input('Par ou Ímpar [P/I] ')).upper().strip()[0]
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar [P/I] ')).upper().strip()[0]
    print(f'O computador jogou {npc}')
    print(f'O total deu {soma}')
    if par:
        print('O total deu PAR')
    else:
        print('O total deu ÍMPAR')
    if escolha == 'P':
        if soma % 2 == 0:
            v += 1
            print('Você ganhou!')
        else:
            print('Você perdeu!')
            break
    elif escolha == 'I':
        if soma % 2 == 0:
            print('Você perdeu!')
            break
print('-=-' * 50)
print(f'Você ganhou {v} vez(es)')
print('-=-' * 50)

