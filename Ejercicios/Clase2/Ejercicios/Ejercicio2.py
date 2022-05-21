# Datos de entrada
peso_producto_gramos=100
precio_producto_euros=5.95
peso_kilo_gramos = 1000

#procesar los datos
precio_porducto_x_gramos=precio_producto_euros / peso_kilo_gramos
precio_kilo= precio_porducto_x_gramos * peso_kilo_gramos

#salida
print("El precio correcto es:", round(precio_kilo,2))