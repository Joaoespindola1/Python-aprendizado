n1 = float(input('Qual foi sua primeira nota? '))
n2 = float(input('Qual foi sus segunda nota? '))

media = (n1+n2)/2
print('Sua média foi {:.1f} e vc está '.format(media),end='')
if media < 5:
    print('\033[31mReprovado')
elif 7 > media >= 5:
    print('\033[35mRecuperação')
elif media >= 7:
    print('\033[32mAprovado')