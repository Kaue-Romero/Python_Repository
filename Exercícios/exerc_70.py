print('''
----------------------
Loja de produtos 
----------------------''')
soma = p2 = menor = count = 0
barato = ''
while True:
    p = str(input('Nome do produto: ')).strip()
    preço = float(input('Preço: R$'))
    count += 1
    if preço > 1000:
        p2 += 1
    if count == 1 or preço < menor:
        menor = preço
        barato = p
    soma += preço
    continuar = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'O total da compra deu R${soma:.2f}')
print(f'Temos {p2} produto(s) custando mais de R$1000,00')
print(f'O item mais barato se chama {barato} e custa R${menor:.2f}')

