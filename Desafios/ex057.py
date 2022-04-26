sexo = input('Digite o seu sexo [M/F]: ').strip().upper()[0]

while sexo not in 'MF':
    sexo = input('Dados inválidos! Digite o sexo novamente [M/F]: ').strip().upper()[0]
print('Fim')
