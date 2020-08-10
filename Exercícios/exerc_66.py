n = soma = count = 0
while n != 999:
    n = int(input('Digite um número,[999] para parar: '))
    if n == 999:
        break
    soma += n
    count += 1
print(f'Você digitou {count} números que somando resultam em {soma}')