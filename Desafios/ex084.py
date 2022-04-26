list = []
dados = []
while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Peso: ')))
    if len(list) == 0:
        mai = men = dados[1]
    else:
        if mai < dados[1]:
            mai = dados[1]
        if men > dados[1]:
            men = dados[1]
    list.append(dados[:])
    dados.clear()
    escolha = input('Quer continuar [S/N]? ').strip().upper()[0]
    if escolha == 'N':
        break
print(f'Foram cadastradas {len(list)} pessoas')

print(f'O maior peso foi de {mai}Kg. Peso de ',end='')
for p in list:
    if p[1] == mai:
        print(f'{p[0]}',end=' ')
print()
print(f'O menor peso foi de {men}Kg. Peso de ',end='')
for p in list:
    if p[1] == men:
        print(f'{p[0]}',end=' ')


