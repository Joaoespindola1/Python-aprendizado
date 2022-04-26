nome = str(input('Digite um nome completo:')).strip()
split = nome.split()
print('O primeiro nome é {}'.format(split[0]))
print('O ultimo nome é {}'.format(split[len(split)-1]))
