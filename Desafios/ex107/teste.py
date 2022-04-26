import moeda


preco = float(input('Digite um valor: '))
print(f'O dobro de {preco} é  {moeda.dobro(preco)}')
print(f'A metade de {preco} é {moeda.metade(preco)}')
print(f'Aumentando {preco} em 15% fica {moeda.aumentar(preco, 15)}')
print(f'Diminuindo {preco} em 25% fica {moeda.diminuir(preco, 25)}')