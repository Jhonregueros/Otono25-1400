# test_eliminar_elemento.py
# Archivo de pruebas para la función eliminar_elemento.

import pytest

try:
    from m8_ocurrencias_ej2 import eliminar_elemento
except ImportError:
    pytest.fail(
        "No se pudo importar la función 'eliminar_elemento' del archivo 'student_code_m9_ex2.py'.")


def test_eliminar_multiples_ocurrencias():
    """Prueba eliminando un elemento que aparece varias veces."""
    assert eliminar_elemento([1, 2, 1, 3, 1, 4], 1) == [2, 3, 4]


def test_eliminar_una_ocurrencia():
    """Prueba eliminando un elemento que aparece una sola vez."""
    assert eliminar_elemento(["a", "b", "c"], "b") == ["a", "c"]


def test_elemento_no_existe():
    """Prueba con un elemento que no está en la lista. Debería devolver una copia de la lista."""
    lista = [10, 20, 30]
    assert eliminar_elemento(lista, 40) == [10, 20, 30]


def test_lista_vacia():
    """Prueba con una lista de entrada vacía."""
    assert eliminar_elemento([], 5) == []


def test_eliminar_todos_los_elementos():
    """Prueba el caso en que todos los elementos de la lista deben ser eliminados."""
    assert eliminar_elemento(["x", "x", "x"], "x") == []


def test_no_modifica_lista_original():
    """Verifica que la función no modifica la lista original (importante sobre referencias)."""
    lista_original = ["rojo", "verde", "azul"]
    lista_copia = lista_original.copy()

    eliminar_elemento(lista_original, "verde")

    assert lista_original == lista_copia, "La función no debe modificar la lista original."


# make this module executable
if __name__ == "__main__":
    # If the tests pass, print a success message
    if pytest.main([__file__]) == 0:
        print("✅ Pruebas pasadas para el ejercicio de variables.")
    # If the tests fail, print an error message
    else:
        print("❌ Error en el código")
        print("Este módulo no se puede ejecutar directamente. Usa pytest para correr las pruebas.")
