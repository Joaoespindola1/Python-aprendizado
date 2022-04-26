from funçoes01 import *
from time import sleep
titulo('CONVERSOR DE MEDIDAS')
# Recebe as váriaveis
quantidade = leiaFloat('Digite a quantidade: ')
print('''Milhas       = [mi]
Polegadas    = [in]
Pés          = [ft]
Centímetros  = [cm]
Metros       = [m]
Quilômetros  = [Km]''')
linha()
medida = input(f'Medida: {quantidade}')
linha()
# Printa uma mensagem de erro caso o usuário digite errado
while medida not in 'mi' 'in' 'ft' 'cm' 'm' 'km':
    print('\033[31mErro Digite uma medida válida!\033[m')
    medida = input('Medida = ').strip().lower()
sleep(0.7)
# Converte as medidas e printa na tela formatado
conversor(quantidade, medida=medida)
