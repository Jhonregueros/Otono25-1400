
🔎 Preguntas de Investigación y Experimentación

# Diferencia entre fullmatch y search:
Si en la función validar_email usáramos re.search en lugar de re.fullmatch, ¿qué pasaría si la cadena de entrada fuera "Esto es invalido email@valido.com el resto"? ¿Por qué es fullmatch la elección correcta para una validación de formato estricta?

# Grupos de Captura: 
En el TODO 2, ¿por qué fue importante usar el metacaracter () para "capturar" solo los 5 dígitos, en lugar de usar solo el patrón sin agrupar? Investiga y explica cómo el uso de match.group(1) te permite aislar la información específica que necesitas.

# Clases de Caracteres y Negación: 
En el TODO 3, ¿cómo se logra la "negación" de un conjunto de caracteres (es decir, hacer coincidir todo excepto letras, números o espacios)? ¿Qué ocurriría si intentaras usar la función re.search en lugar de re.sub para esta tarea? Explica por qué re.sub fue la herramienta correcta para la tarea de "limpieza" de texto.