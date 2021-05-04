#!/usr/bin/python

# Tablero: 6 filas x 7 columnas

def dibujarTablero(tablero):
    print('+---------------------+')
    for fila in tablero:
        print('|', end='')
        for celda in fila:
            if celda:
                print(' {} '.format(celda), end='')
            else:
                print('   ', end='')
        print('|')
    print('+---------------------+')

def completarTableroEnOrden(secuencia, tablero):
    for i, columna in enumerate(secuencia):
        soltarFichaEnColumna((i % 2) + 1, columna, tablero)
    return tablero

def soltarFichaEnColumna(ficha, columna, tablero):
    for fila in range(6, 0, -1):
        if tablero[fila - 1][columna - 1] == 0:
            tablero[fila - 1][columna - 1] = ficha
            break

# Devuelve un tablero vacio
def tableroVacio():
    return [[0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]]

def contenido_columna(nro_columna, tablero):
    columna = []
    for fila in tablero:
        columna.append(fila[nro_columna - 1])
    return columna

def contenido_fila(nro_fila, tablero):
    return tablero[nro_fila - 1]

def columnas(tablero):
    columnas = [[], [], [], [], [], [], []]
    for fila in tablero:
        for i, celda in enumerate(fila):
            columnas[i].append(celda)
    return columnas

def filas(tablero):
    return tablero

def validarSecuencia(secuencia):
    for columna in secuencia:
        if columna < 1 or columna > 7:
            return False
    return True

secuencia = [1, 2, 3, 4, 5, 3, 6, 7]
tablero = []

if validarSecuencia(secuencia):
    tablero = completarTableroEnOrden(secuencia, tableroVacio())
    dibujarTablero(tablero)
else:
    print("Error: las columnas deben estar entre el 1 y el 7.")
