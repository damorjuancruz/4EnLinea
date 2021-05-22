#!/usr/bin/env python3

from src.prototipo import soltar_ficha_en_columna, completar_tablero_en_orden

def test_soltar_ficha_en_columna():
    tablero = [[0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 1, 0, 0, 0, 0],
               [0, 1, 2, 0, 0, 0, 0],
               [1, 2, 2, 1, 0, 0, 0]]

    soltar_ficha_en_columna(2, 3, tablero)
    assert tablero == [[0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 2, 0, 0, 0, 0],
                       [0, 0, 1, 0, 0, 0, 0],
                       [0, 1, 2, 0, 0, 0, 0],
                       [1, 2, 2, 1, 0, 0, 0]]

def test_completar_tablero_en_orden():
    secuencia = [1, 2, 3, 4, 5, 3, 6, 7]
    tablero = [[0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0]]

    assert completar_tablero_en_orden(secuencia, tablero) == [[0, 0, 0, 0, 0, 0, 0],
                                                           [0, 0, 0, 0, 0, 0, 0],
                                                           [0, 0, 0, 0, 0, 0, 0],
                                                           [0, 0, 0, 0, 0, 0, 0],
                                                           [0, 0, 2, 0, 0, 0, 0],
                                                           [1, 2, 1, 2, 1, 1, 2]]
