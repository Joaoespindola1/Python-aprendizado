from random import choice
a1 = input('\033[36mPirmeiro aluno:')
a2 = input('\033[35mSegundo aluno:')
a3 = input('\033[31mTerceiro aluno:')
a4 = input('\033[32mQuarto aluno:\033[m')
nomes = [a1, a2, a3, a4]
escolhido = choice(nomes)
print('O aluno escolhido foi {}{}{}!'.format('\033[36m',escolhido,'\033[m'))