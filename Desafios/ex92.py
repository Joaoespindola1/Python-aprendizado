from datetime import datetime

pessoa = {}
pessoa['nome'] = input(('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
pessoa['idade'] = datetime.now().year-nascimento
pessoa['ctps'] = int(input('Carteira de trabalho[0 se não tem]: '))
if pessoa['ctps'] != 0:
    pessoa['contratacao'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário: '))
    aposento = (pessoa['contratacao']+35)
    pessoa['aposentadoria'] = aposento-nascimento
print('-='*30)
for k, v in pessoa.items():
    print(f'{k} = {v}')
