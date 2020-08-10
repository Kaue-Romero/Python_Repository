from datetime import date
atual = date.today().year
nasc = int(input('Ano do nascimento: '))
idade = atual - nasc
if idade == 18:
    print('Seu ano para se alistar é esse. Parabéns!')
elif idade < 18:
    saldo = idade - 18
    print('Passou o tempo de alistamento')
    print('Passou {} anos do alistamento'.format(saldo))
elif idade > 18:
    saldo = idade - 18
    print('Ainda vai se alistar')
    print('Faltam {} anos para se alistar'.format(saldo))
