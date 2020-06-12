from src.bingo import carton
from src.bingo import no_mas_15
from src.bingo import no_menos_15
from src.bingo import elementos_columnas
from src.bingo import elementos_filas

mi_carton = carton

def test_no_menos_15():
    assert no_menos_15(mi_carton) >= 15

def test_no_mas_15():
    assert no_mas_15(mi_carton) <=15

def test_elementos_columnas():
    assert elementos_columnas(mi_carton) == 9

def test_elementos_filas():
    assert elementos_filas(mi_carton) == 3

