lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for c in range(0, 3):
    for l in range(0, 3):
        lista[c][l] = int(input(f'Digite um valor para [{c}, {l}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{lista[c][l]:^5}]', end='')
    print()
