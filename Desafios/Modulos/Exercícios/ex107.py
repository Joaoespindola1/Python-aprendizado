import moeda

numero = float(input('Digite um preço: R$'))
print(f'A metade de {numero} é {moeda.metade(numero)}')
print(f'O dobro de {numero} é {moeda.dobro(numero)}')
print(f'Aumentando {numero} em 15% fica {moeda.aumentar(numero, 15)}')
print(f'Diminuindo {numero} em 20% fica {moeda.diminuir(numero, 20)}')