lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for c in range(0, 3):
    for l in range(0, 3):
        lista[c][l] = int(input(f'Digite um valor para [{c}, {l}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{lista[l][c]:^5}]', end='')
    print()
pares = 0
for n in lista[0]:
    if n % 2 == 0:
        pares += n
for n in lista[1]:
    if n % 2 == 0:
        pares += n
for n in lista[2]:
    if n % 2 == 0:
        pares += n
print(f'A soma de todos os pares da matriz resultam em {pares}')
num = 0
for l in range(0, 3):
    num += lista[l][2]
print(f'A soma dos valores da segunda coluna resultam em {num}')
print(f'O MAIOR valor da segunda coluna é {max(lista[1])}')
