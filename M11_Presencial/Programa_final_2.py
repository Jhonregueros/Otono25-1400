
"""""
---Semana 11: Diseño del Programa Final
Actividad 1: Crear un diagrama de flujo que muestre el flujo de datos y decisiones (condicionales y bucles).
Actividad 2: Escribir el pseudocódigo, detallando la lógica paso a paso.

Entregables:
Diagrama de flujo (formato visual claro).
Pseudocódigo entendible (con la lógica del programa).
"""

"""
---Semana 12: Codigo
Actividad: Comenzar a escribir el código Python basado en el pseudocódigo.

Aplicar:
Funciones (mínimo 2 con retorno de valor).
Condicionales (if, else), bucles (for, while).
Listas, diccionarios o conjuntos (mínimo 1 estructura de datos).
Clases y objetos.
Expresiones regulares.
Manejo de errores con try-except.

Pruebas Iniciales:
Al menos 3 casos de prueba (válidos e inválidos).
Documentar entradas, salidas esperadas y resultados reales.

import re # Necesario para expresiones regulares
import csv # Necesario para guardar en CSV (funcionalidad extra)
import os # Necesario para verificar si el archivo existe

"""
# ----------------------------------------------------
# 1. CLASE Y OBJETOS
# ----------------------------------------------------

class Viaje:
    """Representa un viaje individual de Uber y calcula sus métricas."""
    
    # Constantes
    TASA_IMPUESTOS = 0.153
    GASTO_GASOLINA_POR_MILLA = 0.10
    GASTO_DESGASTE_POR_MILLA = 0.30

    def __init__(self, fecha, distancia, tiempo, tarifa, propina=0.0, promocion=0.0):
        # Atributos básicos (entradas)
        self.fecha = fecha
        self.distancia = distancia
        self.tiempo = tiempo
        self.tarifa = tarifa
        self.propina = propina
        self.promocion = promocion

        # Atributos calculados (se llenan al llamar a calcular_metricas)
        self.puntos_distancia = 0
        self.puntos_tiempo = 0
        self.ganancia_bruta = 0.0
        self.gastos = 0.0
        self.ganancia_neta = 0.0
        self.taxes = 0.0
        self.ganancia_real = 0.0

    # ----------------------------------------------------
    # 2. FUNCIONES CON RETORNO DE VALOR (dentro de la clase)
    # ----------------------------------------------------
    
    def calcular_puntos_distancia(self):
        """Calcula los puntos por la distancia (mínimo 2 con retorno)."""
        if self.distancia < 5:
            return 1
        elif self.distancia <= 15:
            return 2
        else:
            return 3

    def calcular_gastos(self):
        """Calcula los gastos totales del viaje (mínimo 2 con retorno)."""
        gasolina = self.distancia * self.GASTO_GASOLINA_POR_MILLA
        desgaste = self.distancia * self.GASTO_DESGASTE_POR_MILLA
        return gasolina + desgaste

    def calcular_metricas(self):
        """Realiza todos los cálculos y actualiza los atributos del objeto."""
        
        # Puntos
        self.puntos_distancia = self.calcular_puntos_distancia()
        # El cálculo de puntos de tiempo se mantiene como función auxiliar por estructura
        self.puntos_tiempo = calcular_puntos_tiempo(self.tiempo)
        
        # Cálculos financieros
        self.ganancia_bruta = self.tarifa + self.propina + self.promocion
        self.gastos = self.calcular_gastos()
        self.ganancia_neta = self.ganancia_bruta - self.gastos
        self.taxes = self.ganancia_neta * self.TASA_IMPUESTOS
        self.ganancia_real = self.ganancia_neta - self.taxes

        return self.ganancia_real # Retorna la métrica más importante para confirmación

# ----------------------------------------------------
# FUNCIONES AUXILIARES (Fuera de la clase)
# ----------------------------------------------------

def calcular_puntos_tiempo(tiempo):
    """Función auxiliar para calcular puntos por tiempo."""
    # 3. CONDICIONALES (if, elif, else)
    if tiempo < 5:
        return 1
    elif tiempo <= 15:
        return 2
    else:
        return 3

def guardar_a_csv(viajes_list, nombre_archivo="resumen_viajes.csv"):
    """Guarda la lista de objetos Viaje en un archivo CSV."""
    if not viajes_list:
        print("No hay viajes para guardar.")
        return

    # Encabezados (tomados de las claves del diccionario de un objeto)
    fieldnames = list(viajes_list[0].__dict__.keys())

    # 5. ESTRUCTURA DE DATOS (Diccionario - uso de DictWriter)
    modo = 'a' if os.path.exists(nombre_archivo) and os.path.getsize(nombre_archivo) > 0 else 'w'
    
    with open(nombre_archivo, mode=modo, newline='', encoding='utf-8') as archivo_csv:
        writer = csv.DictWriter(archivo_csv, fieldnames=fieldnames)
        
        # Escribir encabezados solo si el archivo es nuevo o está vacío
        if modo == 'w':
            writer.writeheader()
        
        # 6. BUCLE (for) - Itera sobre la lista de objetos
        for viaje in viajes_list:
            writer.writerow(viaje.__dict__) # Convierte el objeto a diccionario para escribir

    print(f"\n✅ Datos guardados exitosamente en '{nombre_archivo}'.")


def mostrar_resumen_semanal(viajes):
    """Calcula y muestra el resumen de todos los viajes."""
    total_ganancia_bruta = sum(v.ganancia_bruta for v in viajes)
    total_gastos = sum(v.gastos for v in viajes)
    total_ganancia_neta = sum(v.ganancia_neta for v in viajes)
    total_taxes = sum(v.taxes for v in viajes)
    total_real = sum(v.ganancia_real for v in viajes)
    
    # 7. ESTRUCTURA DE DATOS (Lista)
    print("\n======= RESUMEN SEMANAL =======")
    print(f"Total de viajes: {len(viajes)}")
    print(f"Ganancia bruta total: ${total_ganancia_bruta:.2f}")
    print(f"Gastos totales:       ${total_gastos:.2f}")
    print(f"Ganancia neta:        ${total_ganancia_neta:.2f}")
    print(f"Impuestos (15.3%):    ${total_taxes:.2f}")
    print(f"Ganancia real final:  ${total_real:.2f}")
    print("================================")

# ----------------------------------------------------
# BUCLE PRINCIPAL Y MANEJO DE ERRORES
# ----------------------------------------------------

def main():
    viajes = [] # 7. ESTRUCTURA DE DATOS (Lista de objetos Viaje)
    print("=== Control de Ganancias Uber (v2.0) ===")

    # 6. BUCLE (while) para la entrada de datos
    while True:
        print("\n--- Ingrese los datos del viaje ---")
        
        # 8. EXPRESIONES REGULARES y MANEJO DE ERRORES
        while True:
            fecha_input = input("Fecha (YYYY-MM-DD): ")
            # 4. Expresión regular: verifica el formato AAAA-MM-DD
            if re.match(r"\d{4}-\d{2}-\d{2}$", fecha_input):
                break
            else:
                print("❌ Error: Formato de fecha inválido. Use YYYY-MM-DD.")
        
        # 9. MANEJO DE ERRORES (try-except) para entradas numéricas
        try:
            distancia = float(input("Distancia (millas): "))
            tiempo = float(input("Duración (minutos): "))
            tarifa = float(input("Tarifa del viaje ($): "))

            # Preguntar por opcionales con manejo de errores simple
            propina_s = input("¿Recibió propina? (s/n): ").lower()
            propina_valor = float(input("Valor propina ($): ")) if propina_s == "s" else 0.0

            promo_s = input("¿Recibió promoción/bono? (s/n): ").lower()
            promo_valor = float(input("Valor bono ($): ")) if promo_s == "s" else 0.0

        except ValueError:
            print("❌ Error: Por favor, ingrese valores numéricos válidos para distancia, tiempo, tarifa, propina o bono.")
            continue # Vuelve al inicio del bucle

        # 5. CLASE Y OBJETOS - Crear e inicializar el objeto Viaje
        viaje_actual = Viaje(fecha_input, distancia, tiempo, tarifa, propina_valor, promo_valor)
        
        # Ejecutar cálculos
        ganancia_final = viaje_actual.calcular_metricas()
        
        # Guardar el objeto en la lista
        viajes.append(viaje_actual)

        # Mostrar resumen del viaje
        print("\n=== RESUMEN DEL VIAJE ===")
        print(f"Fecha: {viaje_actual.fecha}")
        print(f"Distancia: {viaje_actual.distancia:.1f} millas ({viaje_actual.puntos_distancia} pts)")
        print(f"Tiempo: {viaje_actual.tiempo:.1f} min ({viaje_actual.puntos_tiempo} pts)")
        print(f"Ganancia real:  ${ganancia_final:.2f}")
        print("============================")

        # Preguntar si desea ingresar otro viaje
        continuar = input("\n¿Desea ingresar otro viaje? (s/n): ").lower()
        if continuar != "s":
            break

    # Mostrar y guardar resultados
    if viajes:
        mostrar_resumen_semanal(viajes)
        guardar_a_csv(viajes) # Guarda los datos automáticamente
    
    print("\n=== FIN DEL PROGRAMA ===")


if __name__ == "__main__":
    main()

"""
Entregables:
Código parcial funcional.
Lista con pruebas realizadas.

---Semana 13: Finalización y Documentación
Actividad: Completar el programa y asegurar que todo funcione correctamente.

Comentar el código adecuadamente.
Hacer pruebas finales con valores extremos y casos límite.
Escribir el archivo README.md con:
Descripción del programa.
Instrucciones de uso.
Documentación técnica básica.

Entregables:
Código final completo y funcional.
Archivo README.md.
Lista final de pruebas con entradas/salidas esperadas.

-- Semana 14: Presentacion de su programa (continuacion)
La presentacion debe ser dentro de 5-10 minutos
Asegurate de mostrar capturas de pantalla del código o diagramas.
Y de responder las siguientes preguntas:

1. Concepción e Inspiración: Establecer el contexto y la justificación del proyecto.
- ¿Cuál fue la chispa inicial o el problema central que te llevó a crear este juego, programa o solución?
- ¿Cómo se originó la idea? 

2. Público Objetivo y Diseño: Demostrar un entendimiento del usuario y del mercado/necesidad.
- ¿A quién está dirigido este proyecto? Definición del público/usuario objetivo.
- ¿Cómo influyó el público objetivo en las decisiones de diseño y funcionalidad?
        
3. Proceso y Desarrollo: Informar sobre la robustez del proyecto y la capacidad de resolución de problemas.
- ¿Dónde y cómo se integraron los requisitos o pasos obligatorios del curso/proyecto
(por ejemplo, el uso de Git, ciertas estructuras de datos, etc.)?
- Muestra la estructura del proyecto y las decisiones técnicas clave.
- Probar el cumplimiento de las especificaciones y la aplicación de los conocimientos.

4. Calidad y Lecciones Aprendidas
- ¿Qué pruebas se ejecutaron (unitarias, integración, aceptación, etc.) y
cuáles fueron los resultados iniciales?
- Presenta una lista de los errores (bugs) críticos que encontraste y explica brevemente
la solución implementada para cada uno.
   
5. Feedback y Proyección a Futuro
- ¿Qué sugerencias, dudas o retroalimentación recibiste de las personas que probaron tu código o producto por primera vez?
- Si tuvieras más tiempo, ¿cuáles serían las mejoras o nuevas funcionalidades prioritarias que implementarías?

"""