from random import randint
print('='*35)
print('{:=^35}'.format(' Par ou impar '))
print('='*35)
c = 0
while True:
    comp = randint(0, 10)
    escolha = input('Par ou ímpar? [P/I] ').upper().strip()[0]
    while escolha not in 'PI':
        escolha = input('Par ou ímpar? [P/I] ').upper().strip()[0]
    n = int(input('Escolha seu número: '))
    print(f'Você escolheu {n} e o computador escolheu {comp}')
    print('Deu par' if (comp+n) % 2 == 0 else 'Deu impar' )
    if escolha == 'P':
        if (n + comp) % 2 == 0:
            print('Você ganhou!')
        else:
            print('Você perdeu!')
            break
    if escolha == 'I':
        if (n + comp) % 2 != 0:
            print('Você ganhou!')
        else:
            print('Você perdeu!')
            break
    c += 1
    print('=-='*15)
print('='*25)
print(f'Você teve {c} vitórias consecutivas!')