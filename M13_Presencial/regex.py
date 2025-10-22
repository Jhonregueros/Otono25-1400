import re

# ==============================================================================
# PROYECTO: VALIDADOR DE DATOS CON EXPRESIONES REGULARES (REGEX)
# Este proyecto simula un validador de entradas de usuario usando el módulo 're'.
# ==============================================================================

def validar_email(email):
    """
    TODO 1: Implementar la validación de formato de correo electrónico.
    El patrón debe buscar una estructura básica:
    [caracteres]+ @ [caracteres]+ . [2-4 caracteres]
    
    Pista: Usa \w para caracteres alfanuméricos y \. para el punto literal.
    """
    # Patrón REGEX:
    patron_email = r"^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,4}$" # [Tu código va aquí]
    
    # re.fullmatch comprueba si TODA la cadena coincide con el patrón.
    if re.fullmatch(patron_email, email):
        return True
    return False

def extraer_id_producto(texto):
    """
    TODO 2: Implementar la extracción de un código de producto.
    El patrón debe buscar un código que empiece con "PROD-" seguido de
    exactamente 5 dígitos (por ejemplo, "PROD-12345").
    
    Pista: Usa \d{5} para 5 dígitos y paréntesis () para CAPTURAR el grupo de interés.
    """
    # Patrón REGEX:
    patron_id = r"PROD-(\d{5})" # [Tu código va aquí]
    
    # re.search busca el patrón en cualquier parte de la cadena.
    match = re.search(patron_id, texto)
    if match:
        # match.group(1) retorna el texto capturado por el primer paréntesis.
        return match.group(1) 
    return None

def limpiar_caracteres_especiales(cadena):
    """
    TODO 3: Implementar la limpieza de caracteres especiales.
    El patrón debe buscar y reemplazar cualquier caracter que NO sea
    una letra (a-z, A-Z), un número (0-9) o un espacio, por un guion bajo (_).
    
    Pista: Usa [^...] para la negación de una clase de caracteres.
    """
    # Patrón REGEX para caracteres no permitidos:
    patron_limpieza = r"[^a-zA-Z0-9\s]" # [Tu código va aquí]
    
    # re.sub(patrón, reemplazo, cadena) reemplaza todas las coincidencias.
    cadena_limpia = re.sub(patron_limpieza, '_', cadena)
    return cadena_limpia

# --- Pruebas del Programa ---

datos_a_validar = [
    ("ejemplo.prueba-123@dominio.com", validar_email, "Email"), # Válido
    ("invalido@.c", validar_email, "Email"),                   # Inválido
    ("mi-texto PROD-87654 final.", extraer_id_producto, "ID de Producto"),
    ("PROD-00000 es el primer ID.", extraer_id_producto, "ID de Producto"),
    ("Texto $con #caracteres @raros.", limpiar_caracteres_especiales, "Limpieza de Cadena")
]

print("--- RESULTADOS DE VALIDACIÓN ---")

# Ejecución de Pruebas
for dato, funcion, tipo in datos_a_validar:
    if tipo == "Email":
        resultado = funcion(dato)
        estado = "Válido ✅" if resultado else "Inválido ❌"
        print(f"📧 Email: '{dato}' -> {estado}")
    
    elif tipo == "ID de Producto":
        resultado = funcion(dato)
        print(f"🏷️ Texto: '{dato}' -> ID Extraído: {resultado}")

    elif tipo == "Limpieza de Cadena":
        resultado = funcion(dato)
        print(f"🧼 Original: '{dato}' -> Limpio: '{resultado}'")

# Pregunta de Investigación 1: Prueba de Negación (Para la Pregunta 2 del README)
print("\n--- PRUEBA DE BÚSQUEDA MÚLTIPLE ---")
texto_con_varios_ids = "El ID principal es PROD-11111 y el secundario es PROD-99999."
id_extraido = extraer_id_producto(texto_con_varios_ids)
print(f"🔍 En '{texto_con_varios_ids}', re.search solo extrajo: {id_extraido}. ¿Por qué solo uno?")
