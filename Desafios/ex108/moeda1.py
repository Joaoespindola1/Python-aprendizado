def aumentar(num=0, porcent=0):
    aumento = num + num*(porcent/100)
    return aumento


def diminuir(num=0, porcent=0):
    diminui = num - num*(porcent/100)
    return diminui

def dobro(num=0):
    dobra = num*2
    return dobra

def metade(num=0):
    meia = num/2
    return meia

def moeda(num=0, moeda = 'R$'):
    return f'{moeda}{num:.2f}'.replace('.', ',')


