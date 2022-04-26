nome = input('Qual é o seu nome? ')

if nome == 'João Pedro':
    print('Seu nome é incrível')
elif nome == 'Gerson' or nome == 'Marvin' or nome == 'Isabelle':
    print('Que nome esquisito!')
elif nome in 'Pedro, Fabio, Marcos':
    print('Nome comun no Brasil')
else:
    print('Nome normal')

print('Tenha um bom dia, {}{}{}!!!'.format('\033[35m',nome,'\033[m'))