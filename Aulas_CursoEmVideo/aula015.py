n = s = 0
while True:
    n = int(input('Digite um número inteiro: '))
    if n == 999:
        break
    s += n
print(f'A soma dos valores foi {s}')

