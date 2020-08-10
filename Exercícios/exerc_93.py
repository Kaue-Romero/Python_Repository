jogador = dict()
gols = []
gols2 = []
v = 0
jogador['Nome'] = str(input('Nome do jogador: ')).title().strip()
jogador['Partidas'] = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for c in range(jogador['Partidas']):
    gols.append(int(input(f'Quantidade de gols na {c + 1}º partida: ')))
    v += gols[0]
    gols2.append(gols[0])
    gols.clear()
jogador['Gols'] = v
print('-=' * 20)
print(jogador)
print('-=' * 20)
print(f'O jogador {jogador["Nome"]} jogou {jogador["Partidas"]} partidas.')
for n in range(jogador['Partidas']):
    print(f'    => Na partida {n + 1}º, fez {gols2[n]}')
print(f'Dando o total de {jogador["Gols"]} gols.')
