p = float(input('Digite o preço: R$'))
d = int(input('Desconto: '))
print('Esse valor com desconto de {}% fica R${:.2f}'.format(d, p - p * (d / 100)))
