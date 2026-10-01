def calcular_total(precio, descuento=0):

    if descuento < 0 or descuento > 1:
        raise ValueError("El descuento debe estar entre 0 y 1")

    monto_descuento = precio * descuento

    return precio - monto_descuento


total = calcular_total(100, 0.10)

print(f"Total de venta: S/ {total:.2f}")
