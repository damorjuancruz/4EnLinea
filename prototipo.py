# Tablero: 6 filas x 7 columnas

def dibujarTablero(tablero):
    for fila in tablero:
        for celda in fila:
            if celda:
                print(celda, end=' ')
            else:
                print(' ', end=' ')
        print('')

def completarTableroEnOrden(secuencia, tablero):
    for i, columna in enumerate(secuencia):
        if validarColumna(columna):
            soltarFichaEnColumna((i % 2) + 1, columna, tablero)
        else: 
            print("Error: secuencia no valida.")
            exit(1)
    return tablero

def soltarFichaEnColumna(ficha, columna, tablero):
    for fila in range(6, 0, -1):
        if tablero[fila - 1][columna - 1] == 0:
            tablero[fila - 1][columna - 1] = ficha
            break

def validarColumna(columna):
    return columna >= 1 and columna <= 7

def tableroVacio():
    return [[0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]]

secuencia = [1, 2, 3, 4, 5, 3, 6, 7, 8]

dibujarTablero(completarTableroEnOrden(secuencia, tableroVacio()))