n = float(input('Digite um valor: '))
n2 = float(input('Digite outro: '))
escolha = int(input('''
-------/BEM-VINDO AO MENU DE OPERAÇÕES/----------
Escolha o que quer fazer com os valores:
[ 1 ] SOMAR 
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
\033[31m[ 5 ]SAIR DO PROGRAMA \033[34m:'(
\033[37mDigite sua escolha: '''))
while escolha == 4:
    n = float(input('Digite os novos valores: '))
    n2 = float(input('Digite o outro novo: '))
    escolha = int(input('Escolha a opção: '))
if escolha == 1:
    print('A soma dos números é {:.2f}'.format(n + n2))
elif escolha == 2:
    print('A multiplicação dos valores resultam em {}'.format(n * n2))
elif escolha == 3:
    if n > n2:
        print('{} é maior que {}'.format(n, n2))
    elif n == n2:
        print('Os valores são iguais!')
    else:
        print('{} é maior que {}'.format(n2, n))
elif escolha == 5:
    exit('Você escolheu sair do programa.')
else:
    print('Opção inválida!')


