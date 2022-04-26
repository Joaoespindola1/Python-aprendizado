from operator import itemgetter
lista = []
pessoas = {}
listam = []
acima_da_media = []
soma = 0
while True:
    pessoas['nome'] = input('Nome: ')
    pessoas['sexo'] = input('Sexo[M/F]: ').upper().strip()[0]
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    lista.append(pessoas.copy())
    if pessoas['sexo'] == 'F':
        listam.append(pessoas.copy())
    escolha = input('Quer continaur? [S/N]').strip().upper()[0]
    if escolha in 'N':
        break
media = soma / len(lista)
for i in lista:
    if i['idade'] > media:
        acima_da_media.append(i['nome'])

print(f'{len(lista)} pessoas foram cadastradas.')
print(f'A média de idade do grupoo é {media:.2f}')
print('Lista de mulheres:',end=' ')
for i in listam:
    print(f'{i["nome"]}',end=' ')
print()
print(f'Pessoas com idade acima da média {acima_da_media}')
