lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()
    if continuar not in 'SN':
        continuar = str(input('Tente novamente.Quer continuar? [S/N] ')).upper().strip()
    if continuar == 'N':
        break
print('-=' * 20)
print(f'A lista possui {len(lista)} elementos')
print(f'Sendo eles em ordem decrescente é {sorted(lista, reverse=True)}')
if 5 not in lista:
    print('Não encontrei o valor 5 na lista')
else:
    print('Há sim o valor 5 na lista')
