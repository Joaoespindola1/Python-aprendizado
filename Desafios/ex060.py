n = int(input('Digite um número em fatorial: '))
print('{}! = '.format(n),end='')
fat = 1
for i in range(n, 1, -1):
    print('{} x '.format(i),end='')
    fat = fat*i
if i <= 2:
    print('1',end='')
print(' = {}'.format(fat))



