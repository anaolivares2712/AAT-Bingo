# Los ceros representan celdas vacías
# Los unos representan celdas ocupadas

def carton():
    carton = (
        (1,0,1,0,1,0,1,0,1),
        (0,1,0,1,1,0,0,1,1),
        (1,1,0,1,0,1,0,1,0)
    )
    return carton

def no_menos_15(carton):
    cont = 0
    for fila in carton:
        for celda in fila:
            if celda != 0:
                cont += 1
    return cont

def no_mas_15(carton):
    cont = 0
    for fila in carton:
        for celda in fila:
            if celda != 0:
                cont += 1
    return cont

def elementos_columnas(carton):
    cont = 0
    for i in range(9):
        if(carton[0][i] != 0 or carton[1][i] != 0 or carton[2][i] != 0):
            cont += 1
    return cont

def elementos_filas(carton): #Hice un cambio
    cont = 0
    for i in range(3):
        for j in range(9):
            if carton[i][j] != 0:
                cont += 1
                break
    return cont

def entre_1_y_90(carton):
    for i in range(3):
        for j in range(9):
            if carton[i][j] < 0 or carton[i][j] > 90:
                return 1
    return 0

def aumentan_hacia_la_derecha(carton):
    for i in range(3):
        izq = 0
        der = 10
        for j in range(9):
            if carton[i][j] != 0:
                if (carton[i][j] < izq or carton[i][j] > der):
                    return 1
            izq += 10
            der += 10
    return 0

def aumentan_hacia_abajo(carton):
    for j in range(9):
        primero = carton[0][j]
        segundo = carton[1][j]
        tercero = carton[2][j]
        if primero != 0:
            if segundo != 0:
                if primero > segundo:
                    return 1
        if primero != 0:
            if tercero != 0:
                if primero > tercero:
                        return 1
        if segundo != 0:
            if tercero != 0:
                    if segundo > tercero:
                        return 1
    return 0

def numeros_unicos(carton):
    aux = []
    for i in range(3):
        for j in range(9):
            celda = carton[i][j]
            if celda != 0:
                aux.append(celda)
                if aux.count(celda) > 1:
                    return 1
    return 0

def cant_celdas_ocupadas(carton):
    cont = 0
    for i in range(3):
        for j in range(9):
            if carton[i][j] != 0:
                cont += 1
        if cont > 5:
            return 1
        else:
            cont = 0
    return 0

def matriz(carton):
    cont_filas = 0
    cont_columnas = 0
    for fila in carton:
        cont_filas += 1
        for celda in fila:
            cont_columnas += 1
            if cont_columnas > 9:
                return 1
        cont_columnas = 0
    return 0

def columnas_tres_celdas_ocupadas(carton):
    for i in range(9):
        if(carton[0][i] != 0 and carton[1][i] != 0 and carton[2][i] != 0):
            return 1
    return 0

def celdas_vacias_consecutivas(carton):
    cont = 0
    for i in range(3):
        for j in range(9):
            if carton[i][j] == 0:
                cont += 1
                if cont > 2:
                    return 1
            else:
                cont = 0
        cont = 0 
    return 0
