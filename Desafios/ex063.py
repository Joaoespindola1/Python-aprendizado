print('{:=^40}'.format(' FIBONACCI '))
n = int(input('Quantos termos deseja mostrar? '))
c = 3
t1 = 0
t2 = 1
print('{}->{}->'.format(t1, t2),end='')
while c <= n:
    t3 = t1+t2
    t1 = t2
    t2 = t3
    print('{}->'.format(t3),end='')
    c += 1
print('Acabou')

#0 - 1 -1 - 2 - 3 - 5 - 8