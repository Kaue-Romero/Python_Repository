s = float(input('Qual é o seu salário atual: '))
if s >= 1250:
    print('Seu novo salário é R${:.2f}'.format(s + s*(10/100)))
else:
    print('Seu novo salário é R${:.2f}'.format(s + s*(15/100)))
