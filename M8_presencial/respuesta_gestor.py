# Programa para gestionar las notas de los estudiantes

def mostrar_menu():
    """
    Muestra el menú principal con las opciones disponibles.
    """
    print("\n" + "="*30)
    print("=== MENÚ ===")
    print("1. Agregar estudiante")
    print("2. Mostrar todos los estudiantes")
    print("3. Eliminar estudiante por nombre")
    print("4. Buscar estudiante por nombre")
    print("5. Salir")
    print("="*30)

def calcular_promedio(lista_notas):
    """
    Calcula el promedio de una lista de notas.
    """
    if len(lista_notas) == 0:
        return None
    suma = 0
    for nota in lista_notas:
        suma += nota
    return suma / len(lista_notas)

def obtener_notas(cantidad_notas):
    """
    Pide al usuario las notas de un estudiante y valida que estén entre 0 y 10.
    """
    notas = []
    for i in range(cantidad_notas):
        while True:
            try:
                nota = float(input(f"Ingrese la nota {i+1}: "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("La nota debe estar entre 0 y 10. Intenta de nuevo.")
            except ValueError:
                print("Por favor ingresa un número válido.")
    return notas

def main():
    """
    Función principal que ejecuta el programa.
    """
    estudiantes = []  # Lista donde se almacenan los estudiantes

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            # Agregar estudiante
            nombre = input("Nombre del estudiante: ")
            cantidad_notas = int(input("¿Cuántas notas va a ingresar el estudiante? "))
            notas = obtener_notas(cantidad_notas)

            # Calcular el promedio
            promedio = calcular_promedio(notas)
            
            # Validar la condición de aprobación
            aprobado = promedio >= 6.0 and all(nota >= 4 for nota in notas)
            
            estudiante = {
                "nombre": nombre,
                "notas": notas,
                "promedio": promedio,
                "aprobado": aprobado
            }
            estudiantes.append(estudiante)
            print(f"\nEstudiante {nombre} agregado correctamente.")
            # Imprimir tipos de datos
            print(f"Tipo de nombre: {type(nombre)}")
            for i, nota in enumerate(notas):
                print(f"Tipo de la nota {i+1}: {type(nota)}")
            print(f"Tipo de promedio: {type(promedio)}")
            print(f"Tipo de aprobación: {type(aprobado)}")

        elif opcion == "2":
            # Mostrar todos los estudiantes
            print("\n=== LISTA DE ESTUDIANTES ===")
            for est in estudiantes:
                estado = "Aprobado" if est["aprobado"] else "Reprobado"
                # Imprimir dos primeras notas con slicing
                print(f"{est['nombre']} - Promedio: {est['promedio']:.2f} - {estado} - Notas: {est['notas'][:2]}")
            
            # Contar aprobados y reprobados
            aprobados = sum(1 for est in estudiantes if est["aprobado"])
            reprobados = len(estudiantes) - aprobados
            print(f"\nTotal Aprobados: {aprobados}")
            print(f"Total Reprobados: {reprobados}")

        elif opcion == "3":
            # Eliminar estudiante por nombre
            nombre_eliminar = input("Ingrese el nombre del estudiante a eliminar: ")
            encontrado = False
            for est in estudiantes:
                if est["nombre"].lower() == nombre_eliminar.lower():
                    estudiantes.remove(est)
                    print(f"Estudiante {nombre_eliminar} eliminado correctamente.")
                    encontrado = True
                    break
            if not encontrado:
                print("Estudiante no encontrado.")

        elif opcion == "4":
            # Buscar estudiante por nombre
            nombre_buscar = input("Ingrese el nombre del estudiante a buscar: ")
            encontrado = False
            for est in estudiantes:
                if est["nombre"].lower() == nombre_buscar.lower():
                    estado = "Aprobado" if est["aprobado"] else "Reprobado"
                    print(f"\nEstudiante encontrado: {est['nombre']}")
                    print(f"Notas: {est['notas']}")
                    print(f"Promedio: {est['promedio']:.2f}")
                    print(f"Estado: {estado}")
                    encontrado = True
                    break
            if not encontrado:
                print("Estudiante no encontrado.")

        elif opcion == "5":
            # Salir
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

main()
