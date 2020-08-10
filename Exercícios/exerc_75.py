n = int(input('Digite um número: ')), int(input('Digite outro número: ')), \
    int(input('Digite mais um número: ')), int(input('Digite o último número: '))
count = v = b = 0
print(f'Você digitou {n}')
print(f'O valor 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'O valor 3 apareceu na {n.index(3) + 1} posição')
else:
    print('O valor 3 não foi digitado')
print('E os números pares foram ', end='')
for c in n:
    if c % 2 == 0:
        print(c, end=' ')

