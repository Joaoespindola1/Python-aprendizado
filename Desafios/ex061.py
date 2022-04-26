n = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite a Razão da P.A: '))
c = 0
termo = 10
while c < termo:
    c += 1
    print('{} -> '.format(n),end='')
    n = n + r

print('Acabou')
