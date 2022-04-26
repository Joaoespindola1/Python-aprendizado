
while True:
    n = int(input('Quer ver a tabuada de que número? '))
    if n < 0:
        break
    print('='*40)
    for i in range(1, 11):
        print(' '*14,end='')
        print(f'{n} x {i} = {n*i}')
    print('=' * 40)
print('\nPrograma encerrado')