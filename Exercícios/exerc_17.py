import math
c1 = float(input('Digite a medida do cateto oposto: '))
c2 = float(input('Digite a medida do cateto adjacente: '))
h = c1**2 + c2**2
print('A medida da hipotenusa é:{:.2f}'.format(math.sqrt(h)))
