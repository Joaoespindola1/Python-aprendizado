nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em Maiúsculo é:{}'.format(nome.upper()))
print('Seu nome em Minúsculo é:{}'.format(nome.lower()))

print('Seu nome tem {} letras'.format(len(nome)-(nome.count(' '))))

pnome = nome.split()
print('Seu primeiro nome tem {} letras'.format(len(pnome[0])))
