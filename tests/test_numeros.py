from src.bingo import carton
from src.bingo import entre_1_y_90
from src.bingo import aumentan_hacia_abajo
from src.bingo import aumentan_hacia_la_derecha
from src.bingo import numeros_unicos
from src.bingo import cant_celdas_ocupadas
from src.bingo import matriz
from src.bingo import columnas_tres_celdas_ocupadas
from src.bingo import celdas_vacias_consecutivas
from src.bingo import celdas_ocupadas_consecutivas

mi_carton = carton

def test_entre_1_y_90():
    assert entre_1_y_90(mi_carton) == 0

def test_aumenta_hacia_la_derecha():
    assert aumentan_hacia_la_derecha(mi_carton) == 0

def test_aumenta_hacia_abajo():
    assert aumentan_hacia_abajo(mi_carton) == 0

def test_numeros_unicos():
    assert numeros_unicos(mi_carton) == 0

def test_cant_celdas_ocupadas():
    assert cant_celdas_ocupadas(mi_carton) == 0

def test_matriz():
    assert matriz(mi_carton) == 0

def test_columnas_tres_celdas_ocupadas():
    assert columnas_tres_celdas_ocupadas(mi_carton) == 0

def test_celdas_vacias_consecutivas():
    assert celdas_vacias_consecutivas(mi_carton) == 0


def test_celdas_ocupadas_consecutivas():
    assert celdas_ocupadas_consecutivas(mi_carton) == 0