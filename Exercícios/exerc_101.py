from datetime import date

idade = date.today().year


def voto(nasc=int(input('Ano em que nasceu: '))):
    if idade - nasc < 18:
        return print(f'Com {idade - nasc} anos: VOTO NEGADO')
    elif idade - nasc > 60:
        return print(f'Com {idade - nasc} anos: VOTO OPCIONAL')
    if idade - nasc >= 18:
        return print(f'Com {idade - nasc} anos: VOTO OBRIGATÓRIO')


voto()
