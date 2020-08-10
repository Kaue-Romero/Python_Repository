lista = []
par = []
ímpares = []
while True:
    lista.append(int(input('Digite um número: ')))
    continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if continuar not in 'SN':
        continuar = str(input('Tente novamente.Quer continuar? [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'A lista completa é {lista}')
for n in lista:
    if n % 2 == 0:
        par.append(n)
    else:
        ímpares.append(n)
print(f'A lista de pares é: {par}')
print(f'E a lista de ímpares é: {ímpares}')
