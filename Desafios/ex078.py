list = []
c = 0
for r in range(0,5):
    list.append(int(input('Digite um valor: ')))
    if c == 0:
        maior = list[0]
        menor = list[0]
    if list[r] >= maior:
        maior = list[r]
    if list[r] <= menor:
        menor = list[r]
    c += 1
print(f'Você digitou os vlaores {list}')
print(f'O maior valor foi {maior} nas posições ',end='')
for i, v in enumerate(list):
    if v == maior:
        print(f'{i}...',end='')
print()
print(f'O menor valor foi {menor} nas posições ',end='')
for i, v in enumerate(list):
    if v == menor:
        print(f'{i}...',end='')
