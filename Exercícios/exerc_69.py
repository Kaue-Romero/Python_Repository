acima = f = g = 0
print('''
----------------------
CADASTRE UMA PESSOA
----------------------''')
i = int(input('Idade: '))
s = str(input('Sexo [M/F]: ')).strip().upper()[0]
while s not in 'MF':
    s = str(input('Sexo inválido digite novamente [M/F]: ')).strip().upper()[0]
    if s == 'F':
        if i < 20:
            g += 1
    else:
        acima += 1
continuar = input('Quer continuar ? [S/N]').strip().upper()[0]
if i >= 18:
    f += 1
while continuar not in 'SN':
    continuar = str(input('Quer continuar ? [S/N]')).strip().upper()[0]
while continuar == 'S':
    print('''
----------------------
CADASTRE UMA PESSOA
----------------------''')
    i = int(input('Idade: '))
    s = str(input('Sexo: [M/F]')).strip().upper()[0]
    while s not in 'MF':
        s = str('Sexo inválido digite novamente [M/F]: ').strip().upper()[0]
    if s == 'F':
        if i < 20:
            g += 1
    else:
        acima += 1
    continuar = str(input('Quer continuar ? [S/N]')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar ? [S/N]')).strip().upper()[0]
    if i >= 18:
        f += 1
if continuar == 'N':
    print('-=-' * 50)
    print('Analisando os dados das pessoa, existem:')
    print(f'{f} pessoa(s) com ou mais de 18')
    print(f'{g} mulher(es) com menos de 20 anos')
    print(f'E {acima + 1} homens cadastrados')
    print('-=-' * 50)
