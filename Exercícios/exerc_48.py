soma = 0
count = 0
for c in range(1, 50, 2):
    if c % 3 == 0:
        count = count + 1
        soma = soma + c
print('A soma de {} valores é {}'.format(count, soma))
