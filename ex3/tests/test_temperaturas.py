import pytest

from temperaturas import dia_do_maior, maior


@pytest.mark.parametrize(
    ("temps", "valor", "dia"),
    [
        ([21, 25, 19, 30, 22], 30, 3),
        ([18], 18, 0),
        ([30, 21], 30, 0),
        ([20, 30], 30, 1),
        ([25, 30, 30, 20], 30, 1),
    ],
)
def test_temperaturas(temps, valor, dia):
    assert maior(temps) == valor
    assert dia_do_maior(temps) == dia


def test_listas_vazias():
    with pytest.raises(ValueError, match="^lista vazia$"):
        maior([])
    with pytest.raises(ValueError, match="^lista vazia$"):
        dia_do_maior([])