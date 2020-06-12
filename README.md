[![Build Status](https://travis-ci.org/anaolivares2712/AAT-Bingo.svg?branch=master)](https://travis-ci.org/anaolivares2712/AAT-Bingo)
La verdad es que no se porque me dice failing cuando los test pasaron correctamente
# Bingo
Proyecto para la materia de Adaptación al Ambiente de Trabajo del Instituto Politécnico Superior Gral. San Martín.
Consiste en un generador de cartones de bingo programado en `Python 3`.
## Reglas 
El cartón que genera cumple con las siguientes reglas:
* Los números del carton se encuentran en el rango 1 a 90.
* Cada columna de un carton (contando de izquierda a derecha) contiene numeros que van del 1 al 9, 10 al 19, 20 al 29 ..., 70 al 79 y 80 al 90.
* No hay números repetidos en el carton.
* Cada fila de un carton tiene exactamente 5 celdas ocupadas.
* Cada carton es una matrix de 3 x 9.
* Cada carton tiene 15 celdas ocupadas.
* Los números de las columnas izquierdas son menores que los de las columnas a la derecha.
* Para una misma columna, sus números están ordenados de menor a mayor de arriba hacia abajo.
* No pueden existir columnas vacias.
* No pueden existir columnas con sus tres celdas ocupadas.
* Cada carton debe tener 3 y solo 3 columas con solo una celda ocupada.
* En una fila no existen más de dos celdas vacías consecutivas.
* En una fila no existen más de dos celdas ocupadas consecutivas.
## Uso
Para clonar el repositorio:
```
git clone https://github.com/anaolivares2712/AAT-Bingo.git
```
Para ejecutar el programa:
```
python src/bingo.py
```
Para ejecutar los test es necesario tener instalada la herramienta `pytest`, lo cual se puede hacer con el comando:
```
pip install -U pytest
```
Una vez instalado se pueden ejecutar los test con el comando:
```
pytest
```
## Ejemplo de salida:
```
[2, 0, 27, 0, 43, 0, 61, 74, 0]
[0, 14, 29, 0, 49, 54, 0, 79, 0]
[0, 19, 0, 32, 0, 57, 62, 0, 88]
```
