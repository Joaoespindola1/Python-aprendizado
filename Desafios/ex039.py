from datetime import date
ano = int(input('Em que ano você nasceu? '))
hoje = date.today().year
alist = hoje-ano
if alist == 18:
    print('Está no ano de se alistar!!!')
elif alist > 18:
    print('Ja passou do ano de se alistar!')
    print('Ja se passaram {} anos desde o seu ano de alistamento, Você deveria se alistar em {}!'.format(alist-18,hoje-(alist-18)))
elif ano-hoje < 18:
    print('Ainda chegará seu ano de se alistar!')
    print('Faltam {} anos para o seu alistamento'.format(18-alist))
