m = 0
m20 = 0
iv = 0
cm = 0
cf = 0
for i in range(1, 5):
    print('------ {}° Pessoa ------'.format(i))
    nome = input('Nome: '.format(i))
    idade = int(input('Idade: '.format(i)))
    sexo = input('Sexo[M/F]: '.format(i))
    m += idade
    if sexo.upper() == 'F':
        if idade < 20:
            m20 += 1
        cf += 1

    if i == 1:
        iv = idade
        velho = nome
    if sexo.upper() == 'M':
        cm += 1
        if idade > iv:
            velho = nome
            iv = idade

media = m/4
print('\nA média da idade do grupo é {}'.format(media))

if 2 > m20 > 0:
    print('{} Mulher tem menos de 20 anos.'.format(m20))
else:
    print('{} Mulheres tem menos de 20 anos.'.format(m20))
if cf == 0:
    print('Não tem mulheres no grupo.')

if cm > 0:
    print('O homem mais velho tem {} anos e se chama {}.'.format(iv,velho.title()))
else:
    print('Não tem homens no grupo.')