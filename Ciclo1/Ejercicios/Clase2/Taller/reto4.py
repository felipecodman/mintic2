# Datos entrada

total_refrescos= 9 * 24
personas = 56

operacion = int(total_refrescos / personas)
misma_cantidad = personas * operacion
sobrante = total_refrescos - misma_cantidad

print("La cantidad que sobro de latas de refresco es ", sobrante)