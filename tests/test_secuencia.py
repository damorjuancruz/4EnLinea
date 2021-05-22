#!/usr/bin/env python3

from src.prototipo import validar_secuencia

def test_validar_secuencia():
    secuencia1 = [1, 2, 3, 4, 5, 3, 6, 7]
    secuencia2 = [1, 2, 3, 4, 5, 6, 7, 8]

    assert validar_secuencia(secuencia1)
    assert not validar_secuencia(secuencia2)
