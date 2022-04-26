# Le uma variavél real, se não for digitada uma variável real da erro e pede q digite um número válido
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
# Printa uma linha para separação
def linha():
    print('-'*36)
# Converte as medidas
def conversor(num, medida):
    if medida in 'm':
        medida = 'metro(s)'
        m = num
        km = m * 0.001
        cm = m * 100
        mi = km * 0.625
        inch = cm * 0.393
        ft = m * 3.28
    elif medida in 'cm':
        medida = 'centimetro(s)'
        cm = num
        km = cm * 0.00001
        m = cm * 0.01
        mi = km * 0.625
        inch = cm * 0.393
        ft = m * 0.032
    elif medida in 'km':
        medida = 'quilômetro(s)'
        km = num
        cm = km * 100000
        m = km * 1000
        mi = km * 0.625
        inch = cm * 0.393
        ft = cm * 0.032
    elif medida in 'mi':
        medida = 'milha(s)'
        mi = num
        cm = mi * 160000
        m = mi * 1600
        km = mi * 1.6
        inch = mi * 63360
        ft = mi * 5280
    elif medida in 'ft':
        medida = 'pé(s)'
        ft = num
        cm = ft * 30.48
        m =  ft * 0.3048
        km = ft * 0.0003048
        inch = ft * 12
        mi = ft * 0.0001893
    elif medida in 'in':
        medida = 'polegada(s)'
        inch = num
        cm = inch * 2.54
        m = inch * 0.0254
        km = inch * 0.0000254
        ft = inch * 0.08333
        mi = inch * 0.0000157828
    # Coloca as medidas em um dicionário
    lista = {'m': m, 'cm': cm, 'km': km, 'milha(s)': mi, 'pé(s)': ft, 'polegada(s)': inch}
    # Printa as medidas convertidas
    for k, v in lista.items():
        print(f'\033[33m{num} {medida} \033[m= \033[36m{v:,} {k}\033[m')
# Printa um Título entre linhas
def titulo(msg):
    tam = len(msg)+16
    print('-' * tam)
    print(f'        \033[35m{msg}\033[m')
    print('-' * tam)