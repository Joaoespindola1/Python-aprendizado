d = int(input('Digite a distância da sua viagem em Km: '))

if d>200:
    print('Sua viagem custará R${:.2f}'.format(d*0.45))
else:
    print('Sua viagem custará R${:.2f}'.format(d*0.50))