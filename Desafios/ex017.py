from math import hypot
op = float(input('Comprimento do cateto oposto:'))
adj = float(input('Comprimento do cateto adjascente:'))
hi = hypot(op, adj)
print('A hipotenusa vai medir {:.2f}:'.format(hi))
