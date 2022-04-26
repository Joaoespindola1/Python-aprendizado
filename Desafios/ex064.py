c = n = s = 0
while n != 999:
    n = int(input('Digite um número inteiro [999] para parar: '))
    c += 1
    if n != 999:
        s += n
print('{} Números foram digitados e a soma de todos os valores foi {}'.format(c-1, s))