lista = ('Lápis', 1, 'Estojo', 5, 'Caderno', 8.99, 'Livro', 15.99, 'Borracha', 1.50)

for n,i in enumerate(lista):
    if n % 2 == 0:
        print(f'{i:.<30}R$', end='')
    if n % 2 != 0:
        print(f'{i:>6.2f}')
