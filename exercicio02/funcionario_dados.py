

class Funcionario:
    def __init__(self,nome = "Mario",salario= 2000):
        self.nome = nome
        self.salario = salario
    
    def aumentar_salario(salario,valor_aumento):
        aumento = salario * valor_aumento / 100
        valor_com_aumento = aumento + salario
        return valor_com_aumento
