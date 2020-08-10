from datetime import date
b = date.today().year
tot = 0
tot2 = 0
for c in range(1, 8):
    n = int(input('Digite o ano que a {}ª pessoa: '.format(c)))
    if b - n >= 18:
        tot += 1
    else:
        tot2 += 1
print('{} pessoa já atingiram a maioridade!'.format(tot))
print('E {} pessoas vão atingir!'.format(tot2))
