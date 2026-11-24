import pytest
from veiculo_dados import Carro,Veiculo

carro = Carro()
veiculo = Veiculo()

# @pytest.mark.skip(reason="teste nao finalizado")
def test_veiculo():
    # objeto + classe
    assert isinstance(carro,Veiculo) == True
    assert carro.portas == 4
    assert Carro.ligar() == True