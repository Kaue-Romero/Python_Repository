from datetime import date
nascimento = date.today().year
cadastro = dict()
cadastro['Nome'] = str(input('Nome: ')).strip().title()
cadastro['Ano de nascimento'] = int(input('Ano de nascimento:'))
b = cadastro['Ano de nascimento']
cadastro['CTPS'] = int(input("Carteira de trabalho [0 para não tenho]: "))
if cadastro['CTPS'] != 0:
    cadastro['Ano de contratação'] = int(input('Ano de contratação: '))
    c = cadastro['Ano de contratação']
    cadastro['Salário'] = float(input('Salário: '))
    print(f'Idade: {nascimento - b}')
    print(f'CTPS: {cadastro["CTPS"]}')
    print(f'Salário anual = R${cadastro["Salário"] * 12:.2f}')
    print(f'Você foi admitido em {cadastro["Ano de contratação"]}')
    print(f'Então faltam {b - c + 35} anos para se aposentar!')
elif cadastro['CTPS'] == 0:
    print('Cadastro parcialmente concluído.\nTente novamente adicionando o número da Carteira de trabalho para mais informções.')
    print('Cadastro:')
    print(f'Nome: {cadastro["Nome"]}')
    print(f'Ano de nascimento: {cadastro["Ano de nascimento"]}')
    print(f'Idade: {nascimento - b}')
