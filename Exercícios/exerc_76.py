print('''
-------------------------------
    LISTAGEM DE PREÇOS
-------------------------------''')
i = 'Lápis', 1.75,\
    'Borracha', 2,\
    'Caderno', 15.90,\
    'Estojo', 25,\
    'Transferidor', 4.20,\
    'Compasso', 9.99,\
    'Mochila', 120.32,\
    'Canetas', 22.30,\
    'Livro', 34.90
for item in range(len(i)):
    if item % 2 == 0:
        print(f'{i[item]:.<30}', end='')
    else:
        print(f'R${i[item]:>7.2f}')
