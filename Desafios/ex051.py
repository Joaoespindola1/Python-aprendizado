n = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite a Razão da P.A: '))
f = n+r*10
c = 0
for i in range(n, f, r):
    c += 1
    print('{} -> '.format(i),end='')
print('Acabou')