maior = 0
menor = 0
for c in range(1, 6):
    n = float(input('Qual é o peso da {}ª pessoa? '.format(c)))
    if c == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('O maior peso foi de {}Kg'.format(maior))
print('O menor peso foi de {}Kg'.format(menor))
