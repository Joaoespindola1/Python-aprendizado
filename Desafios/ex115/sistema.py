def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except KeyboardInterrupt:
            return 0
        except:
            print(f'\033[31mErro, digite um número inteiro válido!\033[m')
            continue
        else:
            return num
def cabeçalho(msg):
    print('-' * 40)
    print(msg.center(40))
    print('-' * 40)

def menu(lista):
    cabeçalho('Menu Principal')
    c = 1
    for i in lista:
        print(f'\033[35m{c}\033[m - \033[34m{i}\033[m')
        c += 1
    print('-'*42)
    opc = leiaInt('\033[35mSua Opção:\033[m ')
    return opc