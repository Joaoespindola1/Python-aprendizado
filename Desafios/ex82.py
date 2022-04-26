list = []
lpar = []
limpar = []
while True:
    n = int(input('Digite um número: '))
    list.append(n)
    escolha = 'j'
    while escolha not in 'SN':
        escolha = input('Quer continuar[S/N]? ').strip().upper()[0]
    if escolha == 'N':
        break
for i in list:
    if i % 2 == 0:
        lpar.append(i)
    else:
        limpar.append(i)
print(f'A lista completa {list}')
print(f'A lista dos pares {lpar}')
print(f'A lista dos impares {limpar}')
