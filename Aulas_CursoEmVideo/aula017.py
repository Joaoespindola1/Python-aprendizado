num = []
for c in range(0,5):
    num.append(int(input('Digite um valor: ')))

for p, i in enumerate(num):
    print(f'Na posição {p} encontrei o valor {i}!')
print('Chegamos ao final da lista.')