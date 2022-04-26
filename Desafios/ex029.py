v = int(input('Digite a velocidade do carro em Km/h: '))
if v > 80:
    print('Você foi multado!')
    print('Sua multa custará R${:.2f}'.format((v-80)*7))

