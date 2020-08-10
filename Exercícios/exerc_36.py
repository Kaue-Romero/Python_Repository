casa = float(input('Qual é o valor da casa? '))
s = float(input('Qual o salário do comprador? '))
s2 = s * 30/100
anos = int(input('Em quantos anos vai pagar? '))
valor = casa / (anos * 12)
if valor <= s2:
    print('-=-' * 50)
    print('Você pode parcelar a casa!')
    print('O valor mensal será R${:.2f}'.format(valor))
    print('-=-' * 50)
else:
    print('-=-' * 50)
    print('Você não pode parcelar a casa!')
    print('-=-' * 50)
