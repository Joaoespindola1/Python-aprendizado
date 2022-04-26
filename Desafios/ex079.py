list = []
while True:
    n = (int(input('Digite um valor: ')))
    if n not in list:
        list.append(n)
    else:
        print('Valores duplicado não serão adicionados')
    escolha = 'j'
    while escolha not in 'SN':
        escolha = input('Quer continuar [S/N]? ').strip().upper()[0]
    if escolha in 'N':
        break
list.sort()
print(list)

