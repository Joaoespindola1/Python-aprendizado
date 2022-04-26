from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
print(40*'=')
print('{:=^40}'.format(' JOKENPÔ '))
print(40*'=')
while True:
    comp = randint(0,2)

    print('''Escolha entre "PEDRA" "PAPEL" OU "TESOURA":
- 0 Para Pedra
- 1 Para Papel
- 2 Para Tesoura''')
    escolha = (int(input('Qual sua escolha? ')))

    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('POOOOO\n')
    print('-='*14)
    print('Você escolheu {}'.format(itens[escolha]))
    print('O computador escolheu {}'.format(itens[comp]))
    print('-='*14)

    if escolha == 0:
        if comp == 0:
            print('Empate')
        elif comp == 1:
            print('Você perdeu!')
        elif comp == 2:
            print('Você ganhou!')

    elif escolha == 1:
        if comp == 0:
            print('Você ganhou!')
        elif comp == 1:
            print('Empate')
        elif comp == 2:
            print('Você perdeu!')

    elif escolha == 2:
        if comp == 0:
            print('Você perdeu!')
        elif comp == 1:
            print('Você ganhou!')
        elif comp == 2:
            print('Empate')
    else:
        print('\033[31mOpção Inválida')
    continuar = input('Quer contiuar jogando? [S/N]: ').upper().strip()[0]
    if continuar == 'N':
        break

print('Programa encerrado')
