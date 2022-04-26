frase = 'Curso em Video Python'
print(frase[9:21:2])

tamanho = len(frase)
print(tamanho)

contagem_de_letras = frase.count('o', 0, 14)
print(contagem_de_letras)

encontrar = frase.find('deo')
print(encontrar)

achar = 'curso' in frase
print(achar)

trocar = frase.replace('python', 'android')
print(trocar)

capit = frase.capitalize()
print(capit)

titulo = frase.title()
print(titulo)

frase2 = '  Aprenda Python  '
remove_espacos = frase2.strip()  #rstrip = remove os espacos do lado direito e lstrip do esquerdo
print(remove_espacos)

divisao = frase.split()
print(divisao)

juntar = ' '.join(divisao)
print(juntar)






