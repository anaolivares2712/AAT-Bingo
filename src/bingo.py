import random
import math

def nuevo_carton(): # Creo nuevo cartón
    cont = 0

    carton = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
    ]
    numeros_carton = 0

    while numeros_carton < 15:
        cont += 1
        if cont == 50 :
            return nuevo_carton()
        numero = random.randint(1, 90)

        columna = math.floor(numero / 10)
        if columna == 9:
            columna = 8
        huecos = 0
        for i in range(3):
            if carton[i][columna] == 0:
                huecos += 1
            if carton[i][columna] == numero:
                huecos = 0
                break
        if(huecos < 2):
            continue

        fila = 0
        for j in range(3):
            huecos = 0
            for i in range(9):
                if carton[fila][i] == 0:
                    huecos += 1
            if huecos < 5 or carton[fila][columna] != 0:
                fila += 1
            else:
                break
        if fila == 3:
            continue

        carton[fila][columna] = numero
        numeros_carton += 1
        cont = 0

    for x in range(9):
        huecos = 0
        for y in range(3):
            if carton[y][x] == 0:
                huecos += 1
        if huecos == 3:
            return nuevo_carton()

    return carton

def no_menos_15(carton): # No hay menos de 15 celdas ocupadas en el cartón
    cont = 0
    for fila in carton:
        for celda in fila:
            if celda != 0:
                cont += 1
    return cont

def no_mas_15(carton): # No hay mas de 15 celdas ocupadas en el cartón
    cont = 0
    for fila in carton:
        for celda in fila:
            if celda != 0:
                cont += 1
    return cont

def elementos_columnas(carton): # No pueden existir columnas vacías
    cont = 0
    for i in range(9):
        if(carton[0][i] != 0 or carton[1][i] != 0 or carton[2][i] != 0):
            cont += 1
    return cont

def elementos_3_columnas(carton): # Cada carton debe tener 3 y solo 3 columnas con una sola celda ocupada
    cont = 0
    for columna in range(9):
        cont2 = 0
        for fila in range(3):
            if carton[fila][columna] != 0:
                cont2 += 1
        if cont2 == 1:
            cont += 1
    return cont

def entre_1_y_90(carton): # Los números del cartón se encuentran entre 1 y 90
    for i in range(3):
        for j in range(9):
            if carton[i][j] < 0 or carton[i][j] > 90:
                return 1
    return 0

def aumentan_hacia_la_derecha(carton): # Los números de las columnas izquierdas son menores que los de las columnas hacia la derecha y cada columna del cartón, contando de izquierda da derecha, tiene números que aumentan por decenas
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

def aumentan_hacia_abajo(carton): # Para una misma columna, sus números están ordenados de menor a mayor de arriba hacia abajo
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

def numeros_unicos(carton): # No hay números repetidos en el cartón
    aux = []
    for i in range(3):
        for j in range(9):
            celda = carton[i][j]
            if celda != 0:
                aux.append(celda)
                if aux.count(celda) > 1:
                    return 1
    return 0

def cant_celdas_ocupadas(carton): # Cada fila de un cartón tiene exactamente 5 celdas ocupadas
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

def matriz(carton): # Cada cartón es una matriz de 3x9
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

def columnas_tres_celdas_ocupadas(carton): # No pueden existir columnas con sus tres celdas ocupadas
    for i in range(9):
        if(carton[0][i] != 0 and carton[1][i] != 0 and carton[2][i] != 0):
            return 1
    return 0

def celdas_vacias_consecutivas(carton): # En una fila no existen mas de dos celdas vacías consecutivas
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

def celdas_ocupadas_consecutivas(carton): # En una fila no existen mas de dos celdas ocupadas consecutivas
    cont = 0
    for i in range(3):
        for j in range(9):
            if carton[i][j] != 0:
                cont += 1
                if cont > 2:
                    return 1
            else:
                cont = 0
        cont = 0
    return 0

def tests():
    while True:
        carton = nuevo_carton() # Creo el cartón y compruebo que es válido
        if (no_menos_15(carton) >= 15
        and no_mas_15(carton) <= 15
        and elementos_columnas(carton) == 9
        and elementos_3_columnas(carton) == 3
        and entre_1_y_90(carton) == 0
        and aumentan_hacia_la_derecha(carton) == 0
        and aumentan_hacia_abajo(carton) == 0
        and numeros_unicos(carton) == 0
        and cant_celdas_ocupadas(carton) == 0
        and matriz(carton) == 0
        and columnas_tres_celdas_ocupadas(carton) == 0
        and celdas_vacias_consecutivas(carton) == 0
        and celdas_ocupadas_consecutivas(carton) == 0):
            break
    return carton