from random import randint
from time import sleep

def sorteio(num):
    for i in range(0, 5):
        n = randint(0, 10)
        num.append(n)
    print(f'Os valores sorteados foram {numeros}')
def somaPar(list):
    par = 0
    for i in list:
        if i % 2 == 0:
            par += i
    print(f'A soma dos valores pares de {numeros} é igual a {par}')


numeros = []
sorteio(numeros)
somaPar(numeros)


