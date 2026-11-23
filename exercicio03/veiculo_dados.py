
class Veiculo:
    def __init__(self,marca = "chevrolet",modelo = "camaro"):
        self.marca = marca
        self.modelo = modelo
    
    def ligar(estado):
        if estado == "ligado":
            return True
        else:
            return False

class Carro(Veiculo):
    def __init__(self,portas=4,marca="",modelo=""):
        self.portas = portas
        super().__init__(marca,modelo)
