km = float(input('Digite a distância da viagem em km: '))
if km <= 200:
    print('A viagem custa R${:.2f}'.format(km * 0.50))
else:
    print('A viagem custa R${:.2f}'.format(km * 0.45))
