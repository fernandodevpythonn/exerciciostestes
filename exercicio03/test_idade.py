from maioridade import pessoa

def test_idade():
    assert pessoa(25) >= 18
    assert pessoa(16) >= 18