c = float(input('Preço das compras: R$'))
f = int(input('''FORMAS DE PAGAMENTO
[ 1 ] à vista no dinheiro
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Qual é a opção? '''))
if f == 1:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(c, c - (c * 10 / 100)))
elif f == 2:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(c, c - (c * 5 / 100)))
elif f == 3:
    print('Sua compra de R${:.2f} vai custar R${:.2f} cada parcela, sem acrescimo de juros.'
          'Total de R${:.2f}'.format(c, c / 2, c))
elif f == 4:
    p = int(input('Quantas parcelas? '))
    if p >= 10:
        print('Sua compra ficou em R${:.2f} cada parcela'.format(c / p + (c * 20 / 100)))
    else:
        print('Sua compra ficou em R${:.2f} cada parcela'.format(c / p + (c * 15 / 100)))
else:
    print('Opção inválida!')
