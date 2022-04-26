import math
angulo = float(input('Digite o algulo:'))
print('O COSENA do angulo é {:.2f}'.format(math.cos(math.radians(angulo))),end='')
print(',o SENO é {:.2f}'.format(math.sin(math.radians(angulo))), end=' ')
print('e a TANGENTE {:.2f}'.format(math.tan(math.radians(angulo))))