import moeda


preco = float(input('Digite um valor: R$'))
print(f'O dobro de {moeda.moeda(preco)} é  {moeda.dobro(preco, f=True)}')
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco, f=True)}')
print(f'Aumentando {moeda.moeda(preco)} em 15% fica {moeda.aumentar(preco, 15, f=True)}')
print(f'Diminuindo {moeda.moeda(preco)} em 25% fica {moeda.diminuir(preco, 25, f=True)}')