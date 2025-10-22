"""
PROYECTO DE PROGRAMACIÓN: Cadenas, tuplas, diccionarios y anagramas

Instrucciones:
Lee con atención cada ejercicio. Completa el código en las secciones marcadas como TODO.
Puedes probar tus funciones en la sección "if __name__ == '__main__'".
"""

# ============================
# EJERCICIO 1: Tuplas no hashables
# ============================

def tupla_no_hashable():
    """
    Crea una tupla que contiene listas como elementos. Intenta usarla como clave en un diccionario.
    """
    list0 = [1, 2, 3]
    list1 = [4, 5]
    t = (list0, list1)

    # TODO: Añade el número 6 al final de la segunda lista (list1) usando t
    # Resultado esperado: ([1, 2, 3], [4, 5, 6])

    # TODO: Intenta usar la tupla t como clave en un diccionario y captura el error con try-except
    # Debes imprimir un mensaje que diga que no se puede usar como clave si ocurre un TypeError
    pass


# ============================
# EJERCICIO 2: Cifrado César
# ============================

def shift_word(word, shift):
    """
    Aplica un cifrado César a la palabra dada, desplazando cada letra por 'shift' posiciones.
    Se espera que la palabra esté en minúsculas y sin caracteres especiales.

    Ejemplo:
    shift_word("alegria", 7) -> "alegre"
    shift_word("melon", 16) -> "al cubo"
    """
    # TODO: Implementa el cifrado César aquí
    # Tip: Usa letter_map y operador % para hacer el desplazamiento circular
    letters = 'abcdefghijklmnopqrstuvwxyzáéíóúñ '
    letter_map = dict(zip(letters, range(len(letters))))
    reverse_map = dict(zip(range(len(letters)), letters))
    result = []

    # Recorre cada letra y aplícale el desplazamiento
    for letter in word:
        # TODO: Maneja letras no reconocidas (espacios, tildes, etc.)
        pass

    # Une la lista resultante en una cadena
    return ''.join(result)


# ============================
# EJERCICIO 3: Letras más frecuentes
# ============================

def most_frequent_letters(texto):
    """
    Recibe una cadena y muestra las letras ordenadas por frecuencia (de mayor a menor).
    """
    # TODO: Cuenta las letras ignorando espacios y ordena por frecuencia
    # Tip: Usa value_counts() del ejercicio anterior si lo tienes
    pass


# ============================
# EJERCICIO 4: Anagramas en lista
# ============================

def encontrar_anagramas(lista_palabras):
    """
    Dada una lista de palabras, imprime todos los grupos de palabras que son anagramas.

    Ejemplo de salida:
    ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
    ['retainers', 'ternaries']
    """
    # TODO: Crea un diccionario que relacione la palabra ordenada con sus anagramas
    pass


# ============================
# EJERCICIO 5: Distancia entre palabras
# ============================

def word_distance(word1, word2):
    """
    Devuelve el número de letras distintas entre dos palabras de igual longitud.

    Ejemplo:
    word_distance("casa", "cata") -> 1
    """
    # TODO: Usa zip para comparar letra por letra y contar diferencias
    pass


# ============================
# EJERCICIO 6: Pares de metátesis
# ============================

def encontrar_metatesis(lista_palabras):
    """
    Imprime todos los pares de palabras que son anagramas y difieren solo por una transposición (intercambio de dos letras).

    Ejemplo:
    ('converse', 'conserve')
    """
    # TODO:
    # 1. Encuentra anagramas usando el mismo enfoque del ejercicio anterior
    # 2. Para cada par en cada grupo de anagramas, verifica si son pares de metátesis
    #    (solo deben diferir en exactamente dos letras y ser del mismo largo)
    pass


# ============================
# PRUEBAS
# ============================

if __name__ == '__main__':
    print("EJERCICIO 1: Tupla no hashable")
    tupla_no_hashable()

    print("\nEJERCICIO 2: Cifrado César")
    print(shift_word("alegria", 7))    # Esperado: "alegre"
    print(shift_word("melon", 16))     # Esperado: "al cubo"

    print("\nEJERCICIO 3: Letras más frecuentes")
    most_frequent_letters("el veloz murciélago hindú comía feliz cardillo y kiwi")

    print("\nEJERCICIO 4: Anagramas en lista")
    palabras = ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled', 'retainers', 'ternaries', 'generating', 'greatening', 'resmelts', 'smelters', 'termless']
    encontrar_anagramas(palabras)

    print("\nEJERCICIO 5: Distancia entre palabras")
    print(word_distance("casa", "cata"))  # Esperado: 1
    print(word_distance("luz", "pez"))    # Esperado: 2

    print("\nEJERCICIO 6: Pares de metátesis")
    palabras = ['conserve', 'converse', 'recostar', 'rescatro', 'resmelts', 'smelters', 'termless']
    encontrar_metatesis(palabras)
