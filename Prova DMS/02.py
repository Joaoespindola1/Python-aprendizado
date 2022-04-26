# Importa as funçoes usadas no programa principal
from funçoes02 import *
# Recebe o nome do arquivo
arq = 'disputa.txt'

while True:
    # Mostra um menu
    opc = menu(['Ver disputas', 'Cadastrar nova disputa', 'Finalizar Competição/ Mostrar o Ranking'])
    # Mostra as Disputas
    if opc == 1:
        ler_arquivo(arq)
    # Cadastra uma nova disputa
    elif opc == 2:
        titulo('NOVA DISPUTA')
        time1 = input('Time 1: ')
        gols1 = leiaInt('Gols do time 1: ')
        time2 = input('Time 2: ')
        gols2 = leiaInt('Gols do time 2: ')
        cadastrar(arq, time1, gols1, time2, gols2)
    # Finaliza o programa e mostra o Ranking
    elif opc == 3:
        break
    else:
        print('\033[31mErro! DIGITE UMA OPÇÃO VÁLIDA\033[m')


ranking(arq)
