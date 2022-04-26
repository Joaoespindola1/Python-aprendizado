next = ('Zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    n = int(input('Digite um número entre 0 e 20: '))
    while n > 20 or n < 0:
        n = int(input('Tente novamente! Digite um número entre 0 e 20: '))
    print(f'{n} Por extenso é {next[n]}')
    escolha = input('Quer continaur? ').upper().strip()[0]
    while escolha not in 'NS':
        escolha = input('Quer continaur? ').upper().strip([0])
    if escolha == 'N':
        break
print('Programa encerrado')

