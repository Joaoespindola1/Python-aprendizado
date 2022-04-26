list = []
c = 0
while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    media = (nota1 + nota2) / 2
    list.append([nome, [nota1, nota2], media])
    resp = input('Quer continuar [S/N]? ').strip().upper()[0]
    c += 1
    if resp == 'N':
        break
print('='*30)
print(f'{"Boletim":^30}')
print('='*30)
print(f'{"No":<4}{"Nome":<8}{"Média":>8}')
for i, a in enumerate(list):
    print(f'{i:<4}{a[0]:<4}{a[2]:>8}')
while True:
    escolha = int(input('Deseja ver as notas de que aluno? (999 para parar) '))
    if escolha == 999:
        break
    print(f'As notas de {list[escolha][0]:<4} são {list[escolha][1]} ')
print('Fim do programa')