import pytest

from classificacao import classificar_aluno


@pytest.mark.parametrize(
    ("media", "presenca", "esperado"),
    [
        (8.0, 80, "Aprovado"),
        (10.0, 100, "Aprovado"),
        (0.0, 75, "Reprovado"),
        (7.0, 75, "Aprovado"),
        (5.0, 90, "Recuperacao"),
        (4.99, 90, "Reprovado"),
        (8.0, 74.99, "Reprovado por falta"),
        (0.0, 0, "Reprovado por falta"),
        (0.0, 100, "Reprovado"),
    ],
)
def test_classificacao(media, presenca, esperado):
    assert classificar_aluno(media, presenca) == esperado


@pytest.mark.parametrize(
    ("media", "presenca", "mensagem"),
    [
        (-0.01, 80, "^Media invalida$"),
        (10.01, 80, "^Media invalida$"),
        (8.0, -0.01, "^Presenca invalida$"),
        (8.0, 100.01, "^Presenca invalida$"),
    ],
)
def test_entradas_invalidas(media, presenca, mensagem):
    with pytest.raises(ValueError, match=mensagem):
        classificar_aluno(media, presenca)