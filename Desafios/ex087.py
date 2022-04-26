list = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for c in range(0, 3):
    for i in range (0, 3):
        list[c][i] = int(input(f'Digite o valor da posição [{c}, {i}]:'))
print('='*40)
for c in range(0, 3):
    for i in range (0, 3):
        print(f'[ {list[c][i]:^5} ]',end='')
    print()
soma = somac = maior = 0
for pos, n in enumerate(list):
    if pos == 1:
        for l in n:
            if l > maior:
                maior = l
    for pos, a in enumerate(n):
        if pos == 2:
            somac += a
        if a % 2 == 0:
            soma += a
print('='*40)
print(f'A soma dos valores pares é {soma}')
print(f'A soma dos valores da terceira coluna é {somac}')
print(f'O maior valor da segunda linha é {maior}')

