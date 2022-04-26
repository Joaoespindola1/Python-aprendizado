n = int(input('Digite um número inteiro: '))
print('''Escolha a base de conversão: 
1 - Binário
2 - Octal
3 - hexadecimal''')

base = int(input('Sua escolha: '))

if base == 1:
    print('{} Em Binário ficará {}'.format(n,bin(n)[2:]))
elif base == 2:
    print('{} em Octal ficará {}'.format(n,oct(n)[2:]))
elif base == 3:
    print('{} Em Hexadecimal ficará {}'.format(n,hex(n)[2:]))

else:
    print('Opção Invalida')