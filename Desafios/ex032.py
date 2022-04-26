from datetime import date
ano = int(input('Digite o ano que quer analisar ou 0 para o ano do seu computador:'))
if ano == 0:
    ano = date.today().year

#if ano%4==0:
#    if ano%100>0:
#        print('{} Foi um ano Bissexto!'.format(ano))
#    elif ano%400>0:
#        print('{} Não foi um ano Bissexto'.format(ano))
#    else:
#       print('{} Foi um ano Bissexto'.format(ano))
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print('{} É um ano Bissexto!'.format(ano))
else:
    print('{} Não é um ano Bissexto'.format(ano))

