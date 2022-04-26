jogador = {}
gols = []
jogador['nome'] = input('Nome: ')
jogador['partidas'] = int(input('Quantas partidas ele jogou? '))
for i in range(0, jogador['partidas']):
    gols.append(int(input(f'Gols na partida {i}: ')))
jogador['gols'] = gols
jogador['totalgols'] = sum(gols)
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')
for n, i in enumerate(gols):
    print(f'Na partida {n+1}, fez {i} gols')
print(f'{jogador["nome"]} fez {jogador["totalgols"]} gols no total.')
