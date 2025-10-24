def factura_electricidad():
    """Calcula la factura de electricidad según niveles de consumo."""

    consumo_kwh = int(input("¿Cuántos kWh consumiste este mes? "))

    # Variables de consumo y cargos
    kwh_nivel1 = kwh_nivel2 = kwh_nivel3 = 0
    cargo_nivel1 = cargo_nivel2 = cargo_nivel3 = 0

    # Tarifas por nivel
    tarifa_nivel1 = 0.10
    tarifa_nivel2 = 0.15
    tarifa_nivel3 = 0.20

    # Condiciones para calcular el consumo por nivel
    if consumo_kwh <= 100:
        kwh_nivel1 = consumo_kwh
        cargo_nivel1 = kwh_nivel1 * tarifa_nivel1
    elif consumo_kwh <= 300:
        kwh_nivel1 = 100
        cargo_nivel1 = kwh_nivel1 * tarifa_nivel1
        kwh_nivel2 = consumo_kwh - 100
        cargo_nivel2 = kwh_nivel2 * tarifa_nivel2
    else:
        kwh_nivel1 = 100
        cargo_nivel1 = kwh_nivel1 * tarifa_nivel1
        kwh_nivel2 = 200
        cargo_nivel2 = kwh_nivel2 * tarifa_nivel2
        kwh_nivel3 = consumo_kwh - 300
        cargo_nivel3 = kwh_nivel3 * tarifa_nivel3

    # Total de la factura
    cargo_total = cargo_nivel1 + cargo_nivel2 + cargo_nivel3

    # Función para pluralizar (opcional)
    def pluralizar(kwh):
        return "kWh"

    # Mostrar resumen
    print("\nResumen de tu factura de electricidad:")
    print(f"Consumo total: {consumo_kwh} {pluralizar(consumo_kwh)}")
    print(f"Nivel 1 (0-100): {kwh_nivel1} {pluralizar(kwh_nivel1)}, ${cargo_nivel1:.2f}")
    print(f"Nivel 2 (101-300): {kwh_nivel2} {pluralizar(kwh_nivel2)}, ${cargo_nivel2:.2f}")
    print(f"Nivel 3 (más de 300): {kwh_nivel3} {pluralizar(kwh_nivel3)}, ${cargo_nivel3:.2f}")
    print(f"\nTotal a pagar: ${cargo_total:.2f}")


if __name__ == '__main__':
    factura_electricidad()
