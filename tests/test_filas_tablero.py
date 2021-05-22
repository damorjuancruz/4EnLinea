#!/usr/bin/env python3

from src.prototipo import contenido_fila, filas

def test_contenido_fila():
    tablero = [[0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [2, 1, 2, 1, 0, 2, 0],
               [1, 2, 1, 2, 1, 2, 1]]

    assert contenido_fila(5, tablero) == [2, 1, 2, 1, 0, 2, 0]

def test_filas():
    tablero = [[0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [2, 1, 2, 1, 0, 2, 0],
               [1, 2, 1, 2, 1, 2, 1]]

    assert filas(tablero) == tablero
