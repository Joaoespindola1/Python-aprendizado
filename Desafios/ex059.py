from time import sleep
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
escolha = 0
while escolha != 5:
    print('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa''')
    escolha = int(input('Qual operação deseja realizar? \n'))
    if escolha == 1:
        print('{} + {} = {}'.format(n1, n2, n1+n2))
    elif escolha == 2:
        print('{} * {} = {}'.format(n1, n2, n1*n2))
    elif escolha == 3:
        if n1 > n2:
            print('{} É o maior número'.format(n1))
        else:
            print('{} é o maior número'.format(n2))
    elif escolha == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif escolha == 5:
        print('Finalizando',end='')
        sleep(0.5)
        print('.',end='')
        sleep(0.5)
        print('.',end='')
        sleep(0.5)
        print('.')
    else:
        print('Opção Inválida! Tente novamente')
    print('=-='*10)
    sleep(2)

print('Programa encerrado')