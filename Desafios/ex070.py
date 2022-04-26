print('='*30)
print('{:^30}'.format('Super Lojão'))
print('='*30)
gasto = m1000 = c = barato =  0
while True:
    produto = input('Nome do produto: ')
    preco = int(input('Preço: R$'))
    c += 1
    if c == 1 or preco < barato:
        barato = preco
        pbarato = produto
    gasto += preco
    if preco >= 1000:
        m1000 += 1
    escolha = ' '
    while escolha not in 'SN':
        escolha = input('Quer continuar? [S/N]: ').upper().strip()[0]
    if escolha == 'N':
        break
print(f'O total gasto na compra foi R${gasto:.2f}.')
print(f'{m1000} Produtos custaram mais de R$1000.')
print(f'O produto mais barato foi [{pbarato}] que custa R${barato}.')
