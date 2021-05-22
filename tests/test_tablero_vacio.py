#!/usr/bin/env python3

from src.prototipo import tablero_vacio

def test_tablero_vacio_tiene_6_filas():
    tablero = tablero_vacio()

    assert len(tablero) == 6

def test_tablero_vacio_tiene_7_columnas():
    tablero = tablero_vacio()

    assert len(tablero[0]) == 7
