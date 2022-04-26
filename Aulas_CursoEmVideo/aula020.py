def fun(msg):
    print('_'*40)
    print(f'{msg:^40}')
    print('_'*40)

fun('João Boladão')

def soma(a, b):
    s = a+b
    print(f'A = {a} e B = {b}')
    print(f'A soma de A + B = {s}')


soma(5, 6)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    print(lst)


lista = [2, 3, 4, 8]
dobra(lista)