num = list()
while True:
    n = (int(input('Digite um valor: ')))
    if n not in num:
        num.append(n)
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Tente novamente.Quer continuar ?[S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'Você digitou {sorted(num)}')
