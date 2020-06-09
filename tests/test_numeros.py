from src.bingo import carton
from src.bingo import *

mi_carton = carton()

def test_entre_1_y_90():
    assert entre_1_y_90(mi_carton) == 0

def test_aumenta_hacia_la_derecha():
    mi_carton2 = (
        (3,0,22,0,41,52,0,0,89),
        (7,12,0,38,0,0,0,73,0),
        (0,18,25,0,44,57,64,76,0)
    )
    assert aumentan_hacia_la_derecha(mi_carton2) == 0
