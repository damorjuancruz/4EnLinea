#!/usr/bin/python

# Tablero: 6 filas x 7 columnas

def dibujar_tablero(tablero):
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

def completar_tablero_en_orden(secuencia, tablero):
    for i, columna in enumerate(secuencia):
        soltar_ficha_en_columna((i % 2) + 1, columna, tablero)
    return tablero

def soltar_ficha_en_columna(ficha, columna, tablero):
    for fila in range(6, 0, -1):
        if tablero[fila - 1][columna - 1] == 0:
            tablero[fila - 1][columna - 1] = ficha
            break

# Devuelve un tablero vacio
def tablero_vacio():
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

def validar_secuencia(secuencia):
    for columna in secuencia:
        if columna < 1 or columna > 7:
            return False
    return True

secuencia = [1, 2, 3, 4, 5, 3, 6, 7]
tablero = []

if validar_secuencia(secuencia):
    tablero = completar_tablero_en_orden(secuencia, tablero_vacio())
    dibujar_tablero(tablero)
else:
    print("Error: las columnas deben estar entre el 1 y el 7.")
