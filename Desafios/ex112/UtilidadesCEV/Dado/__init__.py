def leiaDinheiro(msg):
    ok = False
    while not ok:
        valor = str(input(msg)).replace(',', '.').strip()
        if valor.isalpha() or valor == '':
            print('\033[31mErro, Digite um preço válido!\033[m')
        else:
            valor = float(valor)
            ok = True
    return valor