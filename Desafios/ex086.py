list = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for c in range(0, 3):
    for i in range (0, 3):
        list[c][i] = int(input(f'Digite o valor da posição [{c}, {i}]:'))
print('='*40)
for c in range(0, 3):
    for i in range (0, 3):
        print(f'[ {list[c][i]:^5} ]',end='')
    print()


