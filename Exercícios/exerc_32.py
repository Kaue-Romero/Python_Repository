from datetime import date
ano = int(input('Digite o ano que você quer analisar. Digite 0 para saber do ano em q você está: '))
if ano == 0:
    ano = date.today().year
bissexto = ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0
if bissexto:
    print('Você está em um ano bissexto')
else:
    print('Você NÃO está em um ano bissexto')
