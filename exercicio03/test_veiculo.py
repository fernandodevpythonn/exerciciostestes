from veiculo_dados import Carro,Veiculo

carro = Carro()
veiculo = Veiculo()

def test_veiculo():
    assert isinstance(carro,veiculo) == True
