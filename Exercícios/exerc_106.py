def acessar(função):
    help(função)
    return função


while True:
    v = (str(input('Acessar função ou biblioteca> ')))
    if v == 'fim':
        print('\033[:31mVolte Sempre...')
        break
    else:
        acessar(v)
