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


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except KeyboardInterrupt:
            return 0
        except:
            print(f'\033[31mErro, digite um número real válido!\033[m')
            continue
        else:
            return n
