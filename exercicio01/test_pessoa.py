from pessoa import Pessoa_dados

def test_atributos():
    Pessoa_dados("mariana",20)
    dados = Pessoa_dados("Mariana",22)
    assert dados.nome == "Mariana"
    assert dados.idade == 22

