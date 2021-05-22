#!/usr/bin/env python3

from src.prototipo import contenido_columna, columnas

def test_contenido_columna():
    tablero =  [[0, 2, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0],
                [0, 2, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0],
                [0, 2, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0]]

    assert contenido_columna(2, tablero) == [2, 1, 2, 1, 2, 1]

def test_columnas():
    tablero =  [[0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 2, 0],
                [0, 1, 1, 0, 0, 1, 0],
                [1, 2, 2, 2, 2, 1, 2]]

    assert columnas(tablero) == [[0, 0, 0, 0, 0, 1],
                                 [0, 0, 0, 0, 1, 2],
                                 [0, 0, 0, 1, 1, 2],
                                 [0, 0, 0, 0, 0, 2],
                                 [0, 0, 0, 0, 0, 2],
                                 [0, 0, 0, 2, 1, 1],
                                 [0, 0, 0, 0, 0, 2]]
