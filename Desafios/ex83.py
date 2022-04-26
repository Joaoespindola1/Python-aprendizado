expressao = input('Digite a expressão: ')
pilha = []
for i in expressao:
    if i == '(':
        pilha.append('(')
    elif i == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
if len(pilha) > 0:
    print('Sua expressão está invalida!')
elif len(pilha) == 0:
    print('Sua expressão está válida!')