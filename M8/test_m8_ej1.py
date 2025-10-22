# test_filtrar_pares.py
# Archivo de pruebas para la función filtrar_numeros_pares.

import pytest

try:
    from m8_numeros_par_ej1 import filtrar_numeros_pares
except ImportError:
    pytest.fail(
        "No se pudo importar la función 'filtrar_numeros_pares' del archivo 'student_code_m9_ex1.py'.")


def test_lista_mezclada():
    """Prueba con una lista que contiene números pares e impares."""
    assert filtrar_numeros_pares([1, 2, 3, 4, 5, 6]) == [2, 4, 6]


def test_lista_solo_impares():
    """Prueba con una lista que solo contiene números impares."""
    assert filtrar_numeros_pares([1, 3, 5, 7, 9]) == []


def test_lista_solo_pares():
    """Prueba con una lista que solo contiene números pares."""
    assert filtrar_numeros_pares([2, 4, 6, 8]) == [2, 4, 6, 8]


def test_lista_vacia():
    """Prueba con una lista vacía."""
    assert filtrar_numeros_pares([]) == []


def test_con_numeros_negativos():
    """Prueba con números negativos."""
    assert filtrar_numeros_pares([-1, -2, -3, -4, 5, 6]) == [-2, -4, 6]


def test_con_cero():
    """Prueba que el cero se incluye como par."""
    assert filtrar_numeros_pares([0, 1, 2, 3]) == [0, 2]


def test_no_modifica_lista_original():
    """Verifica que la función no modifica la lista original."""
    lista_original = [1, 2, 3, 4]
    lista_original_copia = lista_original.copy()

    filtrar_numeros_pares(lista_original)

    assert lista_original == lista_original_copia, "La función no debe modificar la lista original."


# make this module executable
if __name__ == "__main__":
    # If the tests pass, print a success message
    if pytest.main([__file__]) == 0:
        print("✅ Pruebas pasadas para el ejercicio de variables.")
    # If the tests fail, print an error message
    else:
        print("❌ Error en el código")
        print("Este módulo no se puede ejecutar directamente. Usa pytest para correr las pruebas.")
