'''Pruebas Unitarias Pytest'''
import pytest
import main

@pytest.mark.parametrize("param1, param2",[(0, 0),(0, 1),(1, 1),(1, 0)])
def test_compuertaOr(param1, param2):
    COMPUERTA_OR = main.CompuertaOr(param1, param2)
    assert COMPUERTA_OR.operacion() == 'VERDADERO'

@pytest.mark.parametrize("param1, param2",[(0, 0),(0, 1),(1, 1),(1, 0)])
def test_compuertaAnd(param1, param2):
    COMPUERTA_AND = main.CompuertaAnd(param1, param2)
    assert COMPUERTA_AND.operacion() == 'FALSO'

