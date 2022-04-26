n = int(input('Digite um número inteiro: '))
p = 0
for i in range(1, n+1):
    if n % i == 0:
        p += 1
        print('\033[33m{} \033[m'.format(i),end='')
    else:
        print('\033[31m{} '.format(i),end='')
if p <= 2:
    print('\nÉ um número primo')
else:
    print('\nNão é um número primo')