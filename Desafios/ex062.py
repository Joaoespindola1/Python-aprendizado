yu n = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite a Razão da P.A: '))
c = 0
termo = 10
ct = 10
while c < termo:
    c += 1
    print('{} -> '.format(n),end='')
    n = n + r
    if c == termo:
        print('Pausa')
        termo = int(input('Deseja mostrar mais quantos termos?'))
        ct += termo
        if termo > 0:
            c = 0
        else:
            print('Fim do programa')
print('O programa terminou com {} termos mostrados'.format(ct))