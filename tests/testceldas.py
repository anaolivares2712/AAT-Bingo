from src.bingo import carton

def test_no_menos_15():
    mi_carton = carton()
    cont = 0
    for fila in mi_carton:
        for celda in fila:
            cont += celda
    assert cont >= 15
