n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))

if n1>n2 and n1>n3:
    print('O maior número é o {}'.format(n1))
if n2>n1 and n2>n3:
    print('O maior número é o {}'.format(n2))
if n3>n2 and n3>n1:
    print('O maior número é o {}'.format(n3))

if n1<n2 and n1<n3:
    print('O menor número é o {}'.format(n1))
if n2<n1 and n2<n3:
    print('O menor número é o {}'.format(n2))
if n3<n2 and n3<n1:
    print('O menor número é o {}'.format(n3))