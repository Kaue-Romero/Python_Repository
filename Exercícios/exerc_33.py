n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite mais um número: '))
if n1 < n2:
    if n2 > n3:
        print('{} é o maior!'.format(n2))
    else:
        print('{} é o maior!'.format(n3))
else:
    if n1 > n3:
        print('{} é o maior!'.format(n1))
    else:
        print('{} é o maior!'.format(n3))
if n1 > n2:
    if n2 < n3:
        print('{} é o menor!'.format(n2))
    else:
        print('{} é o menor!'.format(n3))
else:
    if n1 < n3:
        print('{} é o menor!'.format(n1))
    else:
        print('{} é o menor!'.format(n3))
