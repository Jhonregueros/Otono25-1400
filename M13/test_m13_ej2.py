# test_leer_puntajes.py
# Archivo de pruebas para la función promedio_de_archivo.

import pytest

try:
    # TODO: Cambia 'solution_m8_ex2' por 'student_code_m8_ex2' si estás usando el código del estudiante.
    # from solution_m8_ex2 import promedio_de_archivo
    from student_code_m8_ex2 import promedio_de_archivo
except ImportError:
    pytest.fail(
        "No se pudo importar la función 'promedio_de_archivo' del archivo 'student_code_m8_ex2.py'.")


def test_archivo_valido(tmp_path):
    """Prueba la función con un archivo de puntajes válido."""
    # tmp_path es un fixture de pytest que crea un directorio temporal
    directorio = tmp_path / "sub"
    directorio.mkdir()
    archivo_prueba = directorio / "puntajes.txt"
    archivo_prueba.write_text("100\n90\n80\n")

    assert promedio_de_archivo(archivo_prueba) == 90.0


def test_archivo_no_encontrado():
    """Prueba que la función maneja FileNotFoundError."""
    assert promedio_de_archivo(
        "archivo_que_no_existe.txt") == "Error: el archivo no fue encontrado."


def test_archivo_vacio(tmp_path):
    """Prueba con un archivo que existe pero está vacío."""
    archivo_prueba = tmp_path / "vacio.txt"
    archivo_prueba.write_text("")

    assert promedio_de_archivo(archivo_prueba) == 0.0


def test_datos_no_numericos(tmp_path):
    """Prueba con un archivo que contiene datos no numéricos."""
    archivo_prueba = tmp_path / "datos_malos.txt"
    archivo_prueba.write_text("100\nnoventa\n80\n")

    assert promedio_de_archivo(
        archivo_prueba) == "Error: el archivo contiene datos no numéricos."


def test_con_un_solo_puntaje(tmp_path):
    """Prueba con un archivo que contiene un solo puntaje."""
    archivo_prueba = tmp_path / "uno.txt"
    archivo_prueba.write_text("95\n")

    assert promedio_de_archivo(archivo_prueba) == 95.0


# make this module executable
if __name__ == "__main__":
    # If the tests pass, print a success message
    if pytest.main([__file__]) == 0:
        print("✅ Pruebas pasadas para el ejercicio de variables.")
    # If the tests fail, print an error message
    else:
        print("❌ Error en el código")
        print("Este módulo no se puede ejecutar directamente. Usa pytest para correr las pruebas.")
