def ficha(nome='<Não nomeado>', gols=0):
    """
    :param nome: Nome do jogador
    :param gols: Quantidade de gols feitos
    :return: no return
    """
    print(f'O jogador {nome} marcou {gols} gols no campeonato')


n = str(input('Nome do jogador: ')).strip().title()
g = str(input('Gols marcados: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n == '':
    ficha(gols=g)
else:
    ficha(n, g)


