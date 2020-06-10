from src.bingo import carton
from src.bingo import entre_1_y_90
from src.bingo import aumentan_hacia_abajo
from src.bingo import aumentan_hacia_la_derecha
from src.bingo import numeros_unicos
from src.bingo import cant_celdas_ocupadas

mi_carton = carton()

def test_entre_1_y_90():
    assert entre_1_y_90(mi_carton) == 0

def test_aumenta_hacia_la_derecha():
    mi_carton2 = (
        (0,10,0,33,43,0,68,0,81),
        (0,18,22,0,49,52,0,70,0),
        (7,0,26,0,0,57,0,78,84)
    )
    assert aumentan_hacia_la_derecha(mi_carton2) == 0

def test_aumenta_hacia_abajo():
    mi_carton2 = (
        (0,10,0,33,43,0,68,0,81),
        (0,18,22,0,49,52,0,70,0),
        (7,0,26,0,0,57,0,78,84)
    )
    assert aumentan_hacia_abajo(mi_carton2) == 0

def test_numeros_unicos():
    mi_carton2 = (
        (3,0,22,0,41,52,0,0,89),
        (7,12,0,38,0,0,0,73,0),
        (0,18,25,0,44,57,64,76,0)
    )
    assert numeros_unicos(mi_carton2) == 0

def test_cant_celdas_ocupadas():
    assert cant_celdas_ocupadas(mi_carton) == 0
