lista = ('Jogar', 'Aprender', 'Estudar', 'Boneco', 'Amigo', 'Familia', 'Programar')
vogais = ('a', 'e', 'i', 'o', 'u')

for i in lista:
    print(f'\nNa palavra {i.upper()} temos as vogais: ',end='')
    for letras in i:
        if letras.lower() in 'aeiou':
            print(letras.lower(),end=' ')
