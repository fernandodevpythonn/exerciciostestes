from pessoa import pessoa

def test_atributos():
    resultado = pessoa("Mariana",22)
    assert resultado == True