a = float(input('Valor da primeira reta: '))
b = float(input('Valor da segunda reta: '))
c = float(input('Valor da terceira reta: '))
print('-=-' * 50)
if (b - c) < a < b+c:
    if (a - c) < b < a + c:
        if (a - b) < c < a + b:
            print('Podem formar um triângulo :)')
        else:
            print('Elas não podem formar um triângulo')
    else:
        print('Elas não podem formar um triângulo')

else:
    print('Elas não podem formar um triângulo')
print('-=-' * 50)
