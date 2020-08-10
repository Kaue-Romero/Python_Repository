from math import factorial
n = float(input('Digite um número qualquer para ver seu fatorial: '))
print(factorial(n))
continua = str(input('Quer continuar? [S/N] ')).upper()
while continua == 'S':
    n = float(input('Digite outro número: '))
    print(factorial(n))
    continua = str(input('Quer continuar? [S/N] ')).upper()
if continua == 'N':
    exit('Obrigado')
elif continua != 'N' or 'S':
    print('Opção inválida')
else:
    print('Obrigado')
