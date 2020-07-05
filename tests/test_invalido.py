from src.bingo import *

mi_carton2 = (
        (0,0,0,0,0,0,0,0,0),
        (0,0,0,0,0,0,0,0,0),
        (0,0,0,0,0,0,0,0,0)
    )

def test_no_menos_15():
    assert no_menos_15(mi_carton2) != 15

def test_no_mas_15():
    assert no_mas_15(mi_carton2) != 15

def test_elementos_columnas():
    assert elementos_columnas(mi_carton2) != 9

def test_elementos_3_columnas():
    assert elementos_3_columnas(mi_carton2) != 3

def test_entre_1_y_90():
    assert entre_1_y_90(mi_carton2) != 0

def test_aumenta_hacia_la_derecha():
    assert aumentan_hacia_la_derecha(mi_carton2) != 0

def test_aumenta_hacia_abajo():
    assert aumentan_hacia_abajo(mi_carton2) != 0

def test_numeros_unicos():
    assert numeros_unicos(mi_carton2) != 0

def test_cant_celdas_ocupadas():
    assert cant_celdas_ocupadas(mi_carton2) != 0

def test_matriz():
    assert matriz(mi_carton2) != 0

def test_columnas_tres_celdas_ocupadas():
    assert columnas_tres_celdas_ocupadas(mi_carton2) != 0

def test_celdas_vacias_consecutivas():
    assert celdas_vacias_consecutivas(mi_carton2) != 0

def test_celdas_ocupadas_consecutivas():
    assert celdas_ocupadas_consecutivas(mi_carton2) != 0