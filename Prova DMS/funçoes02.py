# Le um valor inteiro ou retorna um erro
def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except KeyboardInterrupt:
            return 0
        except:
            print(f'\033[31mErro, digite um número inteiro válido!\033[m')
            continue
        else:
            return num

# Printa um titulo
def titulo(msg):
    print('-' * 40)
    print(f'\033[36m{msg.center(40)}\033[m')
    print('-' * 40)

# Mostra um menu na tela
def menu(lista):
    titulo('Menu Principal')
    c = 1
    for i in lista:
        print(f'\033[33m{c}\033[m - \033[34m{i}\033[m')
        c += 1
    print('-'*40)
    opc = leiaInt('\033[33mSua Opção:\033[m ')
    return opc

# Le o arquivo e mostra na tela
def ler_arquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        titulo('Disputas cadastradas')
        for linha in a:
            dado = linha.split(';')
            dado[3] = dado[3].replace('\n', '')
            print(f'{dado[0]:<10} - {dado[1]:<5} X {dado[2]:>15} - {dado[3]}')
    finally:
        a.close()

# Cadastra uma disputa no arquivo
def cadastrar(arq, time1='desconhecido', gols1=0, time2='desconhecido', gols2=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um Erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{time1};{gols1};{time2};{gols2}\n')
        except:
            print('Houve um Erro na hora de escrever os dados!')
        else:
            print('Novo registro adicionado. ')

# Mostra um ranking na tela
def ranking(arq):
    try:
        a = open(arq, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        titulo('RANKING FINAL')
        dic = {}
        for linha in a:
            dado = linha.split(';')
            dado[3] = dado[3].replace('\n','')
            dic[dado[0]] = dado[1]
            dic[dado[2]] = dado[3]
        rankin = sorted(dic, key=dic.get, reverse=True)
        for i in rankin:
            print(f'\033[33m{i:<15}\033[m = \033[34m{dic[i]:>7}')










