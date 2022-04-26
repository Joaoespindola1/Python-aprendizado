altura = float(input('Digite sua altura em metros: '))
peso = float(input('Digite seu peso em Kg: '))

imc = peso/(altura*altura)
print('O seu IMC é {:.2f}, seu status é'.format(imc))

if imc < 18.5:
    print('\033[33mAbaixo do peso')
elif 18.5 <= imc < 25:
    print('\033[36mPeso ideal')
elif  25 =< imc < 30:
    print('\033[32mSobrepeso')
elif  30 <= imc < 40:
    print('\033[35mObesidade')
else:
    print('\033[31mObesidade Mórbida')