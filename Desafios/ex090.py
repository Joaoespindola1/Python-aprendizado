aluno = {}
aluno['nome'] = input('Nome: ')
aluno['media'] = float(input('Média: '))
print('-='*30)
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] <7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'
for k, v in aluno.items():
    print(f'{k}: {v}')
