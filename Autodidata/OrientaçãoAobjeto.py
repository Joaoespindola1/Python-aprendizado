class computador:
    def __init__(self):
        self.marca = input('Nome da marca: ')
        self.ram = input('Memória ram: ')
        self.placa_de_video = input('Placa de video: ')

    def exibir(self):
        print(self.marca, self.ram, self.placa_de_video)

    pass




computador1 = computador()

computador1.exibir()