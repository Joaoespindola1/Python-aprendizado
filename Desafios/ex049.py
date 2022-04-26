print('='*40)
print('{:=^40}'.format(' Tabuada '))
print('='*40)
n1 = int(input('Digite o valor:'))

for i in range (1, 11):
    print('{}*{}={}'.format(n1, i, n1*i))