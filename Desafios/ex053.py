frase = input('Digite uma frase: ').strip()

frase = frase.upper().replace(' ', '')
invert = frase[::-1]

print('O inverso de {} é {}'.format(frase, invert))
if frase == invert:
    print('A frase é um Palíndromo')
else:
    print('A frase nao é um Palíndromo')