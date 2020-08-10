notas = dict()
notas['nome'] = str(input('Nome: ')).strip().title()
notas['media'] = float(input(f'Média de {notas["nome"]}: '))
print(f'Nome é igual a {notas["nome"]}')
print(f'Média é igual a {notas["media"]}')
if notas['media'] > 7:
    print('Você está aprovado')
elif notas['media'] <= 4:
    print('Você não passou')
elif notas['media'] < 6:
    print('Você está de recuperação')
