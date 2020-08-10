def msg(tamanho):
    c = len(tamanho) + 4
    print('~' * c)
    print(f'  {tamanho}')
    print('~' * c)


msg(tamanho=str(input('Mensagem: ')))
