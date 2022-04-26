s = float(input('Qual o salário do funcionário? '))

if s > 1250:
    print('O novo salário será de R${:.2f}'.format(s*1.10))
else:
    print('O novo salário será de R${:.2f}'.format(s*1.15))
