
from funcionario_dados import Funcionario

def test_aumentar_salario():
    assert Funcionario.aumentar_salario(2000,10) == 2200
