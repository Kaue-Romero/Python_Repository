print('''
---------------------
10 TERMOS DE UMA PA
---------------------''')
t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = t
count = 1
tot = 0
m = 10
while m != 0:
    tot += m
    while count <= tot:
        print('{} - '.format(termo), end='')
        termo += r
        count += 1
    print('PAUSA')
    m = int(input('Quantos termo a mais você quer ver? '))
print('FIM')

