from time import sleep

def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
    if inicio < fim:
        i = inicio
        while i <= fim:
            print(f'{i} ',end='')
            sleep(0.3)
            i += passo
    else:
        i = inicio
        while i >= fim:
            print(f'{i} ',end='')
            sleep(0.3)
            i -= passo
    print()
    print('-='*20)

contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de fazer a contagem!')
n1 = int(input('Inicio: '))
n2 = int(input('Fim: '))
n3 = int(input('Passo: '))
contador(n1, n2, n3)