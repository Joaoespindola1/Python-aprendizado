from datetime import date
ano = int(input('Em que ano você nasceu? '))
hoje = date.today().year
idade = hoje-ano-1

print('Você tem {} anos e sua categoria é '.format(idade),end="")

if idade <= 9:
    print('\033[36mMirim')
elif idade <= 14:
    print('\033[32mInfantil')
elif idade <= 19:
    print('\033[34mJunior')
elif idade <= 25:
    print('\033[035mSênior')
elif idade > 25:
    print('\033[31mMaster')
