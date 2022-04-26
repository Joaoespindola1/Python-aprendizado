from time import sleep
from Desafios.ex115.sistema import *
from Desafios.ex115.arquivo import *

arq = 'arquivo115.txt'
if not arquivo_exist(arq):
    criar_arquivo(arq)

while True:
    opc = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if opc == 1:
        ler_arquivo(arq)
    elif opc == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif opc == 3:
        break
    else:
        print('\033[31mErro! DIGITE UMA OPÇÃO VÁLIDA\033[m')
    sleep(1.5)
print('Volte sempre!')