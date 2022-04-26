def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'Erro, digite um número inteiro!')
        if ok:
            break
    return valor


#Programa principal
num = leiaInt('Digite um número: ')
print(f'Você digitou o número {num}')