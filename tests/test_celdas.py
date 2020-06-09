from src.bingo import carton

mi_carton = carton()

def test_no_menos_15():
    cont = 0
    for fila in mi_carton:
        for celda in fila:
            cont += celda
    assert cont >= 15

def test_no_mas_15():
    cont = 0
    for fila in mi_carton:
        for celda in fila:
            cont += celda
    assert cont <= 15

def test_columnas():
    cont = 0
    for i in range(9):
        if(mi_carton[0][i] == 1 or mi_carton[1][i] == 1 or mi_carton[2][i] == 1):
            cont += 1
    assert cont == 9

def test_filas():
    cont = 0
    for i in range(3):
        for j in range(9):
            if mi_carton[i][j] == 1:
                cont += 1
                break
    assert cont == 3
