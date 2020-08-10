n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
if m < 5:
    print('Reprovado. Sua média foi de {}'.format(m))
elif m >= 5:
    if m < 6.7:
        print('Recuperação. Sua média foi de {}'.format(m))
    else:
        print('Aprovado. Sua média foi de {}'.format(m))
