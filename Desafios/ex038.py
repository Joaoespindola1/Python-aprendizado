n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print('{} é o maior número'.format(n1))
elif n2 > n1:
    print('{} é o maior número'.format(n2))
else:
    print('Os dois números são iguais')