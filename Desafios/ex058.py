import random
n = random.randint(0, 10)
print('Vou pensar em um Número entre 0 e 10 e voce deve tentar adivinhar!')
escolha = int(input('Digite o seu palpite: '))
c = 1
while escolha != n:
    if escolha < n:
        print('Mais...')
    if escolha > n:
        print('Menos...')
    escolha = int(input('Digite outro palpite: '))
    c += 1
print('Acertou, o número escolhido foi {} e você precisou de {} chances para acertar!'.format(n, c))
