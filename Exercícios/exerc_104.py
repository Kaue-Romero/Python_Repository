def leiaint(msg):
    """
    :param msg: Número para ser verificado
    :return: retorna o valor (se o número não for um número inteiro)
    """
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            print(f'O valor que foi digitado foi {n}')
            break
        else:
            ok = False
        if not ok:
            print('\033[:31mERRO: valor númerico inválido.\033[m')
    return valor


n = leiaint('Digite um número: ')
