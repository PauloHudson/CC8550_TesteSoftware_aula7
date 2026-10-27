import pytest

from parcelamento import parcela


@pytest.mark.parametrize(
    ("valor", "n", "esperado"),
    [
        (120, 1, 120.0),
        (120, 2, 60.0),
        (120, 3, 40.0),
        (120, 4, 30.6),
        (120, 12, 11.8),
        (100, 4, 25.5),
        (100, 6, 17.67),
    ],
)
def test_parcela_nos_limites_e_nos_juros(valor, n, esperado):
    assert parcela(valor, n) == esperado


@pytest.mark.parametrize("n", [0, 13])
def test_numero_de_parcelas_invalido(n):
    with pytest.raises(ValueError, match="parcelas invalidas"):
        parcela(120, n)