
try:
    n1 = int(input('Numerador: '))
    n2 =  int(input('Denominador: '))
    r = n1/n2
except (ValueError, TypeError):
    print('Tivemos um problema com o tipo de dado informado!')
except ZeroDivisionError:
    print('Não é possível dividir por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não digitar um valor')
else:
    print(f'O resultador foi {r}')
finally:
    print('Volte sempre! Muito obrigado!')