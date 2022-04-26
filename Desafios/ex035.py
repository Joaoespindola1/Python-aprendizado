r1 = int(input('Primeira reta: '))
r2 = int(input('Segunda reta:' ))
r3 = int(input('Terceira reta:' ))

if r1+r2>r3 and r1+r3>r2 and r2+r3>r1:
    print('As retas {}, {} e {} podem formar um triângulo!'.format(r1, r2, r3))
else:
    print('As retas {}, {} e {} não podem formar um triângulo!'.format(r1, r2, r3))
