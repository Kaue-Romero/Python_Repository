def fatorial(num=1, show=False):
    """
    :param num: Número para ser fatorado
    :param show: Mostar o processo sa fatoração
    :return: Resultado da fatoração
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


n = int(input('Digite um número: '))
print(f'{fatorial(n, show=True)}')
