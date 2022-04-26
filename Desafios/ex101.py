from datetime import datetime
ano = datetime.now().year

def voto(ano_nasc):
    idade =  ano - ano_nasc
    if idade < 16:
        return 'Voto Negado'
    elif idade < 18 or idade > 65:
        return 'Voto Opcional'
    else:
        return 'Voto Obrigatótio'

votagem = int(input('Em que ano você nasceu? '))
idade =  ano - votagem
print(f'com {idade} anos: {voto(votagem)}')

