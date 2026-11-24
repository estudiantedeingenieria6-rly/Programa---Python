def calcular_cantidad_a_pedir(stock_actual: int, stock_minimo: int) -> int:
    """Calcula la cantidad exacta a pedir según el stock actual y el mínimo requerido."""
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    return 0


def generar_reporte_reabastecimiento(inventario: list) -> None:
    """Muestra el nombre de cada artículo y la cantidad exacta a solicitar."""
    print("=== REPORTE DE REABASTECIMIENTO DE INVENTARIO ===")
    for articulo in inventario:
        _, nombre, stock_actual, stock_minimo = articulo
        cantidad_pedir = calcular_cantidad_a_pedir(stock_actual, stock_minimo)
        print(f"Artículo: {nombre} | Cantidad a pedir: {cantidad_pedir}")


def main() -> None:
    # Matriz: [Código del artículo, Nombre del artículo, Stock actual, Stock mínimo requerido]
    inventario = [
        ["ART-01", "Teclado mecánico", 4, 10],
        ["ART-02", "Mouse inalámbrico", 15, 10],
        ["ART-03", "Cable HDMI", 8, 8],
        ["ART-04", "Monitor 24 pulgadas", 2, 6],
        ["ART-05", "Memoria USB 64GB", 20, 12],
    ]

    generar_reporte_reabastecimiento(inventario)


if __name__ == "__main__":
    main()