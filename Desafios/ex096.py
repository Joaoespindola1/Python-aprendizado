def area(a,b):
    m2 = a*b
    print(f'A área do terreno é de {m2}m2')


print('Controle de Terreno')
print('_'*30)
n1 = float(input(('LARGURA(m): ')))
n2 = float(input(('COMPRIMENTO(m): ')))
area(n1, n2)