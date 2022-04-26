from time import sleep
def meio(msg):
    tam = len(msg)+6
    print('\033[7;34;40m',end='')
    print('_'*tam)
    print(f'  {msg}')
    print('_' *tam)

meio('SISTEMA DE AJUDA PyHelp')

while True:
    ajuda = str(input('\033[mFunção ou biblioteca -> ')).strip().lower()
    if ajuda == 'fim':
        print('\033[7;31;40m Programa Finalizado')
        break
    meio(f'Acessando o manual do "{ajuda}"')
    sleep(0.8)
    print('\033[7;35;40m')
    help(ajuda)

