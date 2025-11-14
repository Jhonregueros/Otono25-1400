"""""
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

Entregables:
Código parcial funcional.
Lista con pruebas realizadas."""


# Programa: Control de Ganancias para Conductores Uber
# Autor: Jhon Jairo Regueros
# Descripción: Este programa permite a los conductores registrar viajes y calcular sus ganancias netas y reales.

def calcular_puntos_distancia(distancia):
    if distancia < 5:
        return 1
    elif distancia <= 15:
        return 2
    else:
        return 3

def calcular_puntos_tiempo(tiempo):
    if tiempo < 5:
        return 1
    elif tiempo <= 15:
        return 2
    else:
        return 3

def calcular_gastos(distancia):
    gasolina = distancia * 0.10
    desgaste = distancia * 0.30
    return gasolina + desgaste

def mostrar_resumen(viajes, total_ganancia_bruta, total_gastos, total_ganancia_neta, total_taxes, total_real):
    print("\n======= RESUMEN SEMANAL =======")
    print(f"Total de viajes: {len(viajes)}")
    print(f"Ganancia bruta total: ${total_ganancia_bruta:.2f}")
    print(f"Gastos totales:       ${total_gastos:.2f}")
    print(f"Ganancia neta:        ${total_ganancia_neta:.2f}")
    print(f"Impuestos (15.3%):    ${total_taxes:.2f}")
    print(f"Ganancia real final:  ${total_real:.2f}")
    print("================================")

def main():
    viajes = []
    total_ganancia_bruta = 0
    total_gastos = 0
    total_ganancia_neta = 0
    total_taxes = 0
    total_real = 0

    print("=== Control de Ganancias Uber ===")

    while True:
        print("\nIngrese los datos del viaje:")
        fecha = input("Fecha (YYYY-MM-DD): ")
        distancia = float(input("Distancia (millas): "))
        tiempo = float(input("Duración (minutos): "))
        tarifa = float(input("Tarifa del viaje ($): "))

        # Calcular puntos
        puntos_distancia = calcular_puntos_distancia(distancia)
        puntos_tiempo = calcular_puntos_tiempo(tiempo)

        # Propinas
        propina = input("¿Recibió propina? (s/n): ").lower()
        if propina == "s":
            propina_valor = float(input("Ingrese el valor de la propina ($): "))
        else:
            propina_valor = 0.0

        # Promociones
        promo = input("¿Recibió promoción o bono? (s/n): ").lower()
        if promo == "s":
            promo_valor = float(input("Ingrese el valor del bono ($): "))
        else:
            promo_valor = 0.0

        # Cálculos
        ganancia_bruta = tarifa + propina_valor + promo_valor
        gastos = calcular_gastos(distancia)
        ganancia_neta = ganancia_bruta - gastos
        taxes = ganancia_neta * 0.153
        ganancia_real = ganancia_neta - taxes

        # Guardar datos del viaje
        viajes.append({
            "fecha": fecha,
            "distancia": distancia,
            "tiempo": tiempo,
            "tarifa": tarifa,
            "propina": propina_valor,
            "promocion": promo_valor,
            "bruta": ganancia_bruta,
            "gastos": gastos,
            "neta": ganancia_neta,
            "taxes": taxes,
            "real": ganancia_real,
            "puntos_distancia": puntos_distancia,
            "puntos_tiempo": puntos_tiempo
        })

        # Acumular totales
        total_ganancia_bruta += ganancia_bruta
        total_gastos += gastos
        total_ganancia_neta += ganancia_neta
        total_taxes += taxes
        total_real += ganancia_real

        # Mostrar resumen del viaje
        print("\n=== RESUMEN DEL VIAJE ===")
        print(f"Fecha: {fecha}")
        print(f"Distancia: {distancia} millas ({puntos_distancia} pts)")
        print(f"Tiempo: {tiempo} min ({puntos_tiempo} pts)")
        print(f"Ganancia bruta: ${ganancia_bruta:.2f}")
        print(f"Gastos totales: ${gastos:.2f}")
        print(f"Ganancia neta:  ${ganancia_neta:.2f}")
        print(f"Impuestos:      ${taxes:.2f}")
        print(f"Ganancia real:  ${ganancia_real:.2f}")
        print("============================")

        # ¿Desea agregar otro viaje?
        continuar = input("\n¿Desea ingresar otro viaje? (s/n): ").lower()
        if continuar != "s":
            break

    # Mostrar resumen semanal
    mostrar_resumen(viajes, total_ganancia_bruta, total_gastos, total_ganancia_neta, total_taxes, total_real)
    print("\n=== FIN DEL PROGRAMA ===")


# Ejecutar programa
if __name__ == "__main__":
    main()



"""---Semana 13: Finalización y Documentación
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