from random import shuffle
a1 = input('Pirmeiro aluno:')
a2 = input('Segundo aluno:')
a3 = input('Terceiro aluno:')
a4 = input('Quarto aluno:')
nomes = [a1, a2, a3, a4]
shuffle(nomes)
print('Os alunos escolhidos na ordem foram {}'.format(nomes))