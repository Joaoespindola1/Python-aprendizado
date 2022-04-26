def fatorial(n):
    f = 1
    for i in range(n, 0, -1):
        f *= i
    return f

num = int(input('Digite um valor: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}')