def meio(msg):
    tam = len(msg)+16
    print('-' * tam)
    print(f'        {msg}')
    print('-' * tam)


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

def resumo(num=0, aument=0, reduc=0):
    meio('RESUMO DO VALOR')
    print(f'Valor analisado: \t{moeda(num):>10}')
    print(f'Dobro do valor: \t{dobro(num, True):>10}')
    print(f'Metade do valor: \t{metade(num, True):>10}')
    print(f'{aument}% de aumento: \t{aumentar(num, aument, True):>10}')
    print(f'{reduc}% de redução: \t{diminuir(num, reduc, True):>10}')
    print('-'*31)


