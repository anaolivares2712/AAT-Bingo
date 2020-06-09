from src.bingo import carton
from src.bingo import *

mi_carton = carton()

def test_entre_1_y_90():
    assert entre_1_y_90(mi_carton) == 0
