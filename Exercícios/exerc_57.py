s = str(input('Qual seu sexo [M/F]: ')).strip().upper()[0]
while s != 'M':
    if s == 'F':
        exit(print('Obrigado!'))
    else:
        s = str(input('Sexo inválido. Digite novamente: ')).strip().upper()[0]
print('Obrigado!')

