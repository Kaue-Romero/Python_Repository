pessoa = dict()
soma = v = c = 0
count = [[], [], []]
while True:
    pessoa['Nome'] = str(input('Nome: ')).strip().title()
    pessoa['Sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while pessoa['Sexo'] not in 'MF':
        pessoa['Sexo'] = str(input('Tente novamente.Sexo: [M/F] ')).strip().upper()[0]
    if pessoa['Sexo'] in 'F':
        count[0].append(pessoa['Nome'])
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']
    continuar = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]
    if continuar not in 'SN':
        continuar = str(input('Tente novamente.Quer continuar ? [S/N] ')).strip().upper()[0]
    c += 1
    count[2].append(pessoa.copy())
    if continuar == 'N':
        v = soma / len(count[2])
        break
print(f'{len(count[2])} pessoa(s) foram cadastradas!')
print(f'A média de idade do grupo é {soma / len(count[2]):.2f} anos')
print(f'As mulheres cadastradas foram {count[0]}')
print('A lista de pessoas com idade acima da média:')
for pessoa in count[2]:
    if pessoa['Idade'] >= v:
        print('    ')
        for k, v in pessoa.items():
            print(f'{k} = {v}; ', end='')
