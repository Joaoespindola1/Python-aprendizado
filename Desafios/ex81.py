list = []
while True:
    n = int(input('Digite um número: '))
    list.append(n)
    escolha = 'j'
    while escolha not in 'SN':
        escolha = input('Quer continaur[S/N]?').strip().upper()[0]
    if escolha == 'N':
        break
print(f'Foram digitados ao todo {len(list)} números.')
list.sort(reverse=True)
print(list)
if 5 in list:
    print('O número 5 está na lista e está na posição ',end='')
    p = list.index(5)
    print(p)
else:
    print('O número 5 não está na lista')