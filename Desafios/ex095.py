jogadores = []
jogador = {}
gols = []
while True:
    jogador.clear()
    gols.clear()
    jogador['nome'] = input('Nome: ')
    partidas = int(input('Quantas partidas ele jogou? '))
    for i in range(0, partidas):
        gols.append(int(input(f'    Gols na partida {i+1}: ')))
    jogador['gols'] = gols[:]
    jogador['totalgols'] = sum(gols)
    jogadores.append(jogador.copy())
    escolha = input('Quer continuar? [S/N]').upper().strip()[0]
    if escolha in 'N':
        break
print('-='*30)
print(f'{"Nome":<15}{"Gols":<15}{"Total":<15}')
for k, v in enumerate(jogadores):
    print(f'{k:>0} ',end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
while True:
    dados = int(input('Mostrar dados de qual jogador[999 PARA PARAR]: '))
    if dados == 999:
        break
    while dados >= len(jogadores):
        print('Erro, jogador inexixtente!')
        dados = int(input('Mostrar dados de qual jogador[999 PARA PARAR]: '))
    print(f'----LEVANTAMENTO DO JOGADOR {jogadores[dados]["nome"]} ')
    for n, i in enumerate(jogadores[dados]['gols']):
        print(f'Na partida {n+1}, fez {i} gols')
    print(f'{jogadores[dados]["nome"]} fez {jogadores[dados]["totalgols"]} gols no total.')
    print('-'*50)
print('\nPrograma encerrado!')
