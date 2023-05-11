class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf


class Cliente(Pessoa):
    def __init__(self, nome, cpf, id):
        super().__init__(nome, cpf)
        self.id = id


class Funcionario(Pessoa):
    def __init__(self, nome, cpf, salario):
        super().__init__(nome, cpf)
        self.salario = salario


class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, setor):
        super().__init__(nome, cpf, salario)
        self.setor = setor


class Coordenador(Funcionario):
    def __init__(self, nome, cpf, salario, senha):
        super().__init__(nome, cpf, salario)
        self.senha = senha


class Analista(Funcionario):
    def __init__(self, nome, cpf, salario, full_acess=True):
        super().__init__(nome, cpf, salario)
        self.full_acess = full_acess


pessoa1 = Pessoa('João Pedro', '149.125.220-06')
cliente1 = Cliente('Marcos', '113.115', 15)

print(cliente1.nome)
print(cliente1.id)

