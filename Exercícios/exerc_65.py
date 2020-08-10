resp = 'S'
soma = quant = m = maior = menor = 0
while resp in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar ? [S/N] ')).upper().strip()[0]
m = soma / quant
print('Você digitou {} números e a media foi de {:.2f}'.format(quant, m))
print('O maior número foi {} e o menor foi {}'.format(maior, menor))
