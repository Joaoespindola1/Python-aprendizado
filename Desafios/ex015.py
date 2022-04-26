km = float(input('Digite a quantidade de Km percorridos:'))
dias = int(input('Digite a quantidade de dias que o carro ficou alugado:'))
pt = (km*0.15)+(dias*60)
print('O valor total a ser pago será R${}'.format(pt))