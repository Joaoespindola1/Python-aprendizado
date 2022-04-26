from random import randint
from operator import itemgetter
from time import sleep
jogo = {'Jogador1': randint(1, 6),
        'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6),
        'Jogador4': randint(1, 6)}
for k, v in jogo.items():
    print(f'{k} = {v}')
    sleep(0.8)
ranking = {}
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} = {v[1]}')

