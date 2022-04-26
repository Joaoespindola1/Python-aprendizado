from datetime import date
hoje = date.today().year
c = 0

for i in range(1, 8):
    ano = int(input('Digite o ano de nascimento do N{}:'.format(i)))
    if hoje-ano >= 21:
        c += 1
print('\n{} Pessoas já são maiores de idade e {} ainda não'.format(c, 7-c))