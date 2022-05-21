# Datos entrada

precio_pc=660
porcentaje_descuento =10

# Datos operación
total_porcentaje= porcentaje_descuento / 100
total_descuento= precio_pc * total_porcentaje
precio_total=precio_pc - total_descuento
dato_entero = int(precio_total)

# Datos salida

print("El precio total por pronto pago es de:", dato_entero)