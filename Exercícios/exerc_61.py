print('''
---------------------
10 TERMOS DE UMA PA
---------------------''')
t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = t
count = 1
while count <= 10:
    print('{} - '.format(termo), end='')
    termo += r
    count += 1
print('ACABOU')
