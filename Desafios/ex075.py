n = (int(input('Digite um número: ')),
    int(input('Digite outro número: ')),
    int(input('Mais um número: ')),
    int(input('Digite o ultimo número: ')))

print(f'O número 9 aparece {n.count(9)} vezes na tupla.')
if 3 in n:
    print(f'O número 3 aparece primeiro na {n.index(3)+1}° posição.')
else:
    print('O número 3 não aparece em nenhuma posição.')
print(f'Os números pares foram ',end='')
for i in n:
    if i % 2 == 0:
         print(f'{i}',end='')






