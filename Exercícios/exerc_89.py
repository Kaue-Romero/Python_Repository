nome = list()
nome2 = list()
nota1 = list()
nota2 = list()
nota3 = list()
count = 0
count2 = 0
s = 0
c = 1
while True:
    nome.append(str(input('Nome: ')))
    nota1.append(float(input('Nota 1: ')))
    nota2.append(float(input('Nota 2: ')))
    continuar = str(input('Quer continuar ? [S/N] ')).upper().strip()[0]
    s += 1
    if continuar not in 'SN':
        continuar = str(input('Tente novamente.Quer continuar ? [S/N] ')).upper().strip()[0]
    if continuar not in 'S':
        c = 0
        break
while True:
    for s in nome:
        print(f'{nome[count]} média {(nota1[count] + nota2[count]) / 2:.1f}')
        count += 1
    if c == 0:
        break
while True:
    n = int(input('Mostrar notas de qual aluno? (999 interrompe):'))
    if n == 999:
        print('-=-=-=' * 30)
        print('FINALIZADO... OBRIGADO VOLTE SEMPRE')
        break
    count2 += n
    nome2 = nome[n]
    nota3 = nota1[n], nota2[n]
    print('-=-=-=' * 30)
    print(f'Notas de {nome2} são {nota3}')
    print('-=-=-=' * 30)
