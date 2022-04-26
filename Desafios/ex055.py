for i in range(1, 6):
    peso = float(input('Digite o peso da pessoa N{} em KG: '.format(i)))
    if i == 1:
        mais = peso
        menos = peso

    if peso > mais:
        mais = peso
    if peso < menos:
        menos = peso

print('O maior peso foi {}Kg e o menor foi {}Kg'.format(mais, menos))