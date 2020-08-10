print('''
---------------------
10 TERMOS DE UMA PA
---------------------''')
n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
for c in range(n, n + (10 - 1) * r + r, r):
    print(c, end='-')
print('ACABOU')
