galera = []
dados = []
maior = menor = 0
n = []
n2 = []
while True:
    galera.append(str(input('Digite um nome: ')))
    galera.append(float(input('Peso (Kg): ')))
    if len(dados) == 0:
        menor = maior = galera[1]
    else:
        if galera[1] > maior:
            maior = galera[1]
        if galera[1] < menor:
            menor = galera[1]
    continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if continuar not in 'SN':
        continuar = str(input('Tente novamente.Quer continuar? [S/N]: ')).upper().strip()[0]
    dados.append(galera[:])
    galera.clear()
    if continuar == 'N':
        break
print(f'Você cadastrou {len(dados[:][0])} pessoas')
for p in dados:
    if p[1] == maior:
        n.append(p[0])
    if p[1] == menor:
        n2.append(p[0])
print(f'{len(n)} pessoas foram as mais pesada e são {n} com {maior}Kg')
print(f'E {len(n2)} foram as mais leve e são {n2} com {menor}Kg')
