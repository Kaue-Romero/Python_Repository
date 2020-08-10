i2 = 0
maior = 0
m = 0
f = 0
homemvelho = ''
mulhernova = 0
for c in range(1, 5):
    print('{}ª Pessoa'.format(c))
    n = str(input('Nome: ')).strip()
    i = int(input('Idade: '))
    i2 += i
    s = str(input('Sexo [M/F]: ')).upper().strip()
    if s in 'M':
        m += 1
        if c == 1 and s in 'M':
            maior = i
            homemvelho = n
        if s in 'M' and i > maior:
            maior = i
            homemvelho = n
    else:
        f += 1
        if i < 20:
            mulhernova += 1
print('A media de idade foi de {:.0f} anos!'.format(i2 / 4))
print('Ao todo são {} homem(ns) e {} mulher(es)!'.format(m, f))
print('O homem mais velho se chama {} e tem {} anos de idade'.format(homemvelho, maior))
print('Na lista há {} mulheres com menos de 20 anos'.format(mulhernova))
