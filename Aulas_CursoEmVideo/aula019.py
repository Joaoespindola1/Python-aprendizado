'''pessoas = {'nome': 'João', 'sexo': 'M', 'idade': '20'}
pessoas['peso'] = 93
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.items())
print(pessoas.values())
print(pessoas.keys())
for k, v in pessoas.items():
    print(f'{k} = {v}')'''

estado = {}
brasil = []

for i in range(0, 3):
    estado['uf'] = input('Estado: ')
    estado['sigla'] = input('Sigla: ')
    brasil.append(estado.copy())
for c in brasil:
    for k, v in c.items():
        print(f'{k} = {v}')