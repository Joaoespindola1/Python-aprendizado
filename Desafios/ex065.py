escolha = 's'
m = c = 0

while escolha in 'Ss':
    n = int(input('Digite um número: '))
    escolha = input('Quer continuar[S/N]? ').strip()[0]
    if c == 0:
        maior = menor = n
    if maior < n:
        maior = n
    if menor > n:
        menor = n

    m += n
    c += 1
print('O maior valor foi {} e o menor foi {}!'.format(maior, menor))
print('A média dos valores foi {}'.format(m/c))

