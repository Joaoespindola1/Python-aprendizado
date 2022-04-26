list = [[], []]
for i in range(0,7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        list[0].append(n)
    else:
        list[1].append(n)
list[0].sort()
list[1].sort()
print(f'Os valores pares foram {list[0]}')
print(f'Os valores impares foram {list[1]}')