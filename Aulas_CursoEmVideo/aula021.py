'''def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela
    :param i: Inicio da contagem
    :param f: Final da contagem
    :param p: Passo da contagem
    :return: Sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}, ',end='')
        c += p
help(contador)
def somar(a=0, b=0, c=0):
    s = a+b+c
    return s
r1 = somar(5, 2)
r2 = somar(3,2,5)
r3 = somar(5)
print(f'As somas valem {r1}, {r2} e {r3}')
a = 5
def teste():
    global a
    a = 10
teste()
print(f'A fora vale {a}')'''

def fatorial(num=1):
    f = 1
    for i in range (num, 0, -1):
        f *= i
    return f
n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')


