from time import sleep


def contador():
    c = 1
    c2 = 10
    print('-' * 30)
    print('Contagem de 1 até 10 de 1 em 1')
    while c <= 10:
        print(c, end=' ')
        sleep(0.5)
        c += 1
    print('Fim!')
    sleep(0.5)
    print('Contagem de 10 até 0 de 2 em 2')
    while c2 >= 0:
        print(c2, end=' ')
        c2 -= 2
        sleep(0.5)
    print('Fim!')
    print('Agora é sua vez de personalizar a contagem!')
    c3 = int(input('Início: '))
    c4 = int(input('Fim: '))
    c5 = int(input('Passo: '))
    if c5 < 0:
        c5 *= -1
        print(f'Contagem de {c3} até {c4} de {c5} em {c5}')
    else:
        print(f'Contagem de {c3} até {c4} de {c5} em {c5}')
    if c5 == 0:
        c5 = 1
    if c3 < c4:
        while c3 <= c4:
            print(c3, end=' ')
            c3 += c5
            sleep(0.5)
        print('Fim!')
    elif c3 > c4:
        while c3 >= c4:
            print(c3, end=' ')
            if c5 < 0:
                c3 += c5
            else:
                c3 -= c5
            sleep(0.5)
        print('Fim!')


print(contador())
