num = int(input('Digite um número de 0 a 9999:'))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000

print('Unidade:{}'.format(unidade))
print('Dezena:{}'.format(dezena))
print('centena:{}'.format(centena))
print('Milhar:{}'.format(milhar))