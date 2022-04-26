def aumentar(num=0, porcent=0, f=False):
    aumento = num + num*(porcent/100)
    return aumento if f is False else moeda(aumento)


def diminuir(num=0, porcent=0, f=False):
    diminui = num - num*(porcent/100)
    return diminui if f is False else moeda(diminui)

def dobro(num=0, f=False):
    dobra = num*2
    if f == True:
        dobra = moeda(dobra)
    return dobra

def metade(num=0,f=False):
    meia = num/2
    return meia if f  is False else moeda(meia)

def moeda(num=0, moeda = 'R$'):
    return f'{moeda}{num:.2f}'.replace('.', ',')


