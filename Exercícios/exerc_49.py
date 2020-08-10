n = int(input('Digite um número: '))
soma = 0
for c in range(1, 11):
    c = 1
    soma += c
    print('{} x {} = {}'.format(n, soma, n * soma))
print('-=-' * 20)
