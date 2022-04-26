from time import sleep
from random import randint
print('='*30)
print(f'{"MEGA SENA":^30}')
print('='*30)
escolha = int(input('Quantos jogos deseja fazer? '))
jogo = [0, 0, 0, 0, 0, 0]
print(f'========= Sorteando {escolha} jogos =========')
for c in range(0, escolha):
    print(f'Jogo {c+1}: ',end='')
    for i in range(0, 6):
        num = randint(1, 61)
        while num in jogo:
            num = randint(1, 61)
        else:
            jogo[i] = num
    jogo.sort()
    print(jogo)
    sleep(1)
    jogo = [0, 0, 0, 0, 0, 0]

