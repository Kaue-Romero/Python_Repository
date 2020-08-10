print('Controle de Terrenos!')
print('-' * 30)


def Área(comprimento, largura):
    c = comprimento * largura
    print(f'A área do terreno de {comprimento} cm³x {largura}cm³ é {c:.1f}m²')


Área(comprimento=int(input('Qual o comprimento da parede: ')), largura=int(input('E qual a largura: ')))
