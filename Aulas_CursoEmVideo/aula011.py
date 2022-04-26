# CORES NO TERMINAL
print('\033[36m Olá, mundo!\033[m')
nome = 'Joao Pedro'
cores = {'limpa': '\033[m',
         'roxo': '\033[35m'}
print('Muito prazer em te conhecer, {}{}{}!'.format(cores['roxo'], nome, cores['limpa']))
