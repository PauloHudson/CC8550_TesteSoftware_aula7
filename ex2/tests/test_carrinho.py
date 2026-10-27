from carrinho import total_com_desconto


def test_desconto_progressivo():
    assert total_com_desconto([10, 20, 30, 40, 50]) == 141.0


def test_limite_do_desconto():
    assert total_com_desconto([10, 20, 30, 40]) == 96.0


def test_preco_fracionario_revela_arredondamento():
    assert total_com_desconto([0, 0, 0, 1.01]) == 0.91