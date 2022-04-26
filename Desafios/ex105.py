def notas(*num, sit=False):
    '''
    -> Função para analisar notas e situação de vários alunos
    :param num: Recebe as notas
    :param sit: Se sit=True mostra a situação da turma
    :return: Dicionário com a nota dos alunos
    '''
    notagem = {}
    notagem['total'] = len(num)
    notagem['maior'] = max(num)
    notagem['menor'] = min(num)
    notagem['media'] = sum(num)/len(num)
    if sit:
        if notagem['media'] < 4:
            notagem['sit'] = 'Ruim'
        elif notagem['media'] < 7:
            notagem['sit'] = 'Razoável'
        else:
            notagem['sit'] = 'Boa'
    return notagem


print('_'*40)
nota = notas(7, 9, 8, 3, sit=True)
print(f'{nota}')