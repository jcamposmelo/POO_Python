class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0

    def acelerar(self, incremento):
        self.velocidade += incremento

    def frear(self, decremento):
        self.velocidade -= decremento

    def exibir_informacoes(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Velocidade: {self.velocidade} km/h")


# Criando instâncias da classe Carro
carro1 = Carro("Toyota", "Corolla", 2020)
carro2 = Carro("Honda", "Civic", 2018)

# Acelerando os carros
carro1.acelerar(80)
carro2.acelerar(120)

# Exibindo informações dos carros
carro1.exibir_informacoes()
carro2.exibir_informacoes()

# Freando os carros
carro1.frear(50)
carro2.frear(60)

# Exibindo informações atualizadas dos carros
carro1.exibir_informacoes()
carro2.exibir_informacoes()