def leiaInt(msg):
    ok = False
    while True:
        try:
            n = int(input(msg))
            ok = True
        except KeyboardInterrupt:
            n = 0
            ok = True
        except:
             print(f'\033[31mErro, digite um número inteiro válido!\033[m')
        if ok:
             break
    return n

def leiaFloat(msg):
    ok = False
    while True:
        try:
            n = float(input(msg))
            ok = True
        except KeyboardInterrupt:
            n = 0
            ok = True
        except:
             print(f'\033[31mErro, digite um número real válido!\033[m')
        if ok:
             break
    return n



inteiro = leiaInt('Digite um número inteiro: ')
real = leiaFloat('Digite um número real: ')

print(f'O número inteiro foi {inteiro} e o real foi {real}')

