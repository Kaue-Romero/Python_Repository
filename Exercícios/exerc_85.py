lista = [], [], []
for c in range(0, 7):
    lista[0].append(int(input('Digite um valor: ')))
for c in lista[0]:
    if c % 2 == 0:
        lista[1].append(c)
    else:
        lista[2].append(c)
print(f'Dos valores inseridos {sorted(lista[1])} são par \nE {sorted(lista[2])} são ímpar')
