casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Quanto é o seu salário? R$'))
anos = int(input('Em quantos anos vai pagar o empréstimo? '))
prestacao = casa/(anos*12)

print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(casa,anos,prestacao))
if prestacao > salario*0.30:
    print('Empréstimo \033[31mNegado\033[m!')
else:
    print('Empréstimo \033[36maprovado')

