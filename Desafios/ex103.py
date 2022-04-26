def ficha(nome='<none>' ,gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato!')


j = input('Nome do jogador: ').strip()
g = str(input('Total de Gols no campeonato: '))

if g.isnumeric():
    g = int(g)
else:
    g = 0
if j.strip() == '':
    ficha(gols=g)
else:
    ficha(j, g)