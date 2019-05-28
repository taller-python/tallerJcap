'''Pruebas Unitarias Pytest'''
import pytest
import main

@pytest.mark.parametrize("param1, param2",[(0, 1),(1, 1),(1, 0)])
def test_compuertaOrVerdadero(param1, param2):
    COMPUERTA_OR = main.CompuertaOr(param1, param2)
    assert COMPUERTA_OR.operacion() == 'VERDADERO'

def test_compuertaOrFalso():
    COMPUERTA_OR = main.CompuertaOr(0, 0)
    assert COMPUERTA_OR.operacion() == 'FALSO'

@pytest.mark.parametrize("param1, param2",[(0, 0),(0, 1),(1, 0)])
def test_compuertaAndFalso(param1, param2):
    COMPUERTA_AND = main.CompuertaAnd(param1, param2)
    assert COMPUERTA_AND.operacion() == 'FALSO'

def test_compuertaAndVerdadero():
    COMPUERTA_AND = main.CompuertaAnd(1, 1)
    assert COMPUERTA_AND.operacion() == 'VERDADERO'
