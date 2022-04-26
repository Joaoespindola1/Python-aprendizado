m18 = m20 = m = 0
c = 1
while True:
    idade = int(input(f'Digite a idade da {c}°pessoa: '))
    sexo = input(f'Digite o sexo da {c}°pessoa [M/F]: ').upper().strip()[0]
    while sexo not in 'MF':
        sexo = input(f'Digite o sexo da {c}°pessoa [M/F]: ').upper().strip()[0]
    continuar = input('Quer ler mais dados? [S/N]: ').strip().upper()[0]
    while continuar not in 'SN':
        continuar = input('Quer ler mais dados? [S/N]: ').strip().upper()[0]
    print('=-='*14)
    if sexo == 'M':
        m += 1
    if idade > 18:
        m18 += 1
    if sexo == 'F':
        if idade < 20:
            m20 += 1
    if continuar == 'N':
        break
    c += 1
print(f'{m} Homens foram registrados.')
print(f'{m18} Pessoas tem mais de 18 anos.')
print(f'{m20} Mulheres tem menos de 20 anos.')
print('Programa encerrado')
