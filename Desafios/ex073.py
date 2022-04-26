times = ('América-MG', 'Athletico-PR', 'Atlético-GO', 'Atlético-MG', 'Avaí', 'Botafogo', 'Bragantino', 'Ceará',
         'Corinthians', 'Cuiabá', 'Flamengo', 'Fluminense', 'Fortaleza' , 'Goiás', 'Internacional', 'Juventude',
         'Palmeiras', 'Santos', 'São Paulo')
print(f'Lista de tiems do Brasileirão: {times}')
print('=-'*20)
print(f'Os 5 primeiros colocados são {times[:5]}')
print('=-'*20)
print(f'Os ultimos 4 colocados são {times[-4:]}')
print('=-'*20)
print(f'Times em ordem alfabética {sorted(times)}')
print('=-'*20)
print('O Flamengo está na {}° posição.'.format(times.index('Flamengo')+1))

