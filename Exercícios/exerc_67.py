n = 1
m = 0
while n > 0:
    n = int(input('Quer ver a tabuada de qual valor ? '))
    while m <= 9:
        if n < 0:
            break
        else:
            m += 1
            print(f'{n} x {m} = {n * m}')
    m = 0
print('Tabuada cancelada. Volte sempre')
