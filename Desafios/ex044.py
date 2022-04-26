valor = float(input('Qual o valor do produto? '))
print('''Qual a condição de pagamento? 
 1-> À vista \033[34mDinheiro ou cheque\033[m: 10% de desconto
 2-> À vista no \033[34mcartão\033[m: 5% de desconto
 3-> Em até \033[34m2x no cartão\033[m: preço normal
 4-> \033[34m3x ou mais no cartão\033[m: 20% de Juros''')
pag = int(input('\nComo deseja pagar? '))

if pag == 1:
    valor = valor*0.90
elif pag == 2:
    valor = valor*0.95
elif pag == 4:
    valor = valor*1.20
else:
    print('\033[31mOpção Inválida\033[m')

print('\nO valor final será de R${:.2f}'.format(valor))