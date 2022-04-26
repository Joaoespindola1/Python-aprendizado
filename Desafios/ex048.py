s = 0
for i in range(0, 500, 3):
    if i%2 != 0:
        print(i)
        s += i
        print('Soma = {}'.format(s))

print(s)