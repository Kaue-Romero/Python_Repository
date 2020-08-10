from datetime import date
nascimento = int(input('Digite seu nao de nascimeto: '))
atual = date.today().year
idade = atual - nascimento

if idade <= 9:
    print('Nadador Mirim')
elif idade <= 14:
    print('Nadador infantil')
elif idade <= 19:
    print('Nadador Junior')
elif idade <= 20:
    print('Nadador Sênior')
else:
    print('Nadador Master')
