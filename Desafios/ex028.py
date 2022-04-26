import random
n = random.randint(0, 5)

a = int(input('Digite o número escolhido pelo computador: '))
if a==n:
    print('Você acertou!')
else:
    print('Você errou!')

print('O número escolhido foi {}!'.format(n))