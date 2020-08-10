time = list()
time2 = list()
jogador = dict()
gols = []
gols2 = []
v = 0
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do jogador: ')).title().strip()
    jogador['Partidas'] = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    jogador['Gols'] = gols2
    for c in range(jogador['Partidas']):
        gols.append(int(input(f'Quantidade de gols na {c + 1}º partida: ')))
        v += gols[0]
        gols2.append(gols[0])
        time2.append(gols2.copy())
        gols.clear()
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('Erro! Responda S ou N.')
    if resp == 'N':
        break
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):>15}', end='')
    print()
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Não existe jogador de código {busca}')
    else:
        print(f'----- LEVANTAMENTO DO JOGADOR: {time[busca]["Nome"]}')
        for i, g in enumerate(time[busca]['Gols']):
            print(f'     No jogo {i + 1} fez {g} gols')
