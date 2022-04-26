from random import randint
tnum = (randint(0, 10),randint(0, 10),randint(0, 10),randint(0, 10),randint(0, 10))
print(f'Os valores sorteados foram {tnum}')

print(f'{max(tnum)} É o maior número e {min(tnum)} o menor.')