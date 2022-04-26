import moeda1


preco = float(input('Digite um valor: R$'))
print(f'O dobro de {moeda1.moeda(preco)} é  {moeda1.moeda(moeda1.dobro(preco))}')
print(f'A metade de {moeda1.moeda(preco)} é {moeda1.moeda(moeda1.metade(preco))}')
print(f'Aumentando {moeda1.moeda(preco)} em 15% fica {moeda1.moeda(moeda1.aumentar(preco, 15))}')
print(f'Diminuindo {moeda1.moeda(preco)} em 25% fica {moeda1.moeda(moeda1.diminuir(preco, 25))}')