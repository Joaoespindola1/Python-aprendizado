def fatorial(num,show=False):
    '''
    -> Caclcula o fatorial de um número
    :param num: O número a ser calculado o fatorial
    :param show: (Opcional) True para mostrar a conta
    :return: O fatorial de num
    '''
    f = 1
    for i in range(num, 0, -1):
        f *= i
    if show:
        for i in range(num, 0, -1):
            print(f'{i} x',end=' ')
    else:
        print(f'{num}! ',end='')
    print(f'= {f}')
    return f
fatorial(5, True)
help(fatorial)


