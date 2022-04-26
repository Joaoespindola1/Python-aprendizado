from time import sleep
class carro:
    def __init__(self, marca, cavalos, velocidade_max):
        self.marca = marca
        self.cavalos = cavalos
        self.velocidade_max = velocidade_max
    def exibir_info(self):
        print(f'O carro da marca {self.marca} tem {self.cavalos} cavalos de potência e alcança {self.velocidade_max} de velocidade')

    def ligar(self):
        print(f'Ligando a {self.marca} com {self.cavalos} cavalos!')

    def acelerar(self):
        print(f'Acelerando a {self.marca}')
        sleep(2)
        print('0Km')
        sleep(1)
        print('50Km')
        sleep(1)
        print('100Km')
        sleep(1)
        print('150Km')


carro1 = carro('BMW', '180', '200Km')
carro1.exibir_info()
carro1.ligar()
carro1.acelerar()