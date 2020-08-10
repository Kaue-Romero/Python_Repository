n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro: '))
if n1 < n2:
    print('-=-' * 50)
    print('O segundo valor é maior')
    print('-=-' * 50)
elif n1 > n2:
    print('-=-' * 50)
    print('O primeiro valor é maior')
    print('-=-' * 50)
else:
    print('-=-' * 50)
    print('Os valores são iguais')
    print('-=-' * 50)
