def ejercicio1():
  calculo = 6/2 * (1 + 2)
  print("el resultado correcto es:", calculo)

def ejercicio2(peso_gramos: int, precio: float, conversion: int = 1000) -> float:
    """calcula el precio de un producto en otra unidad
    Parametros:
      Peso_gramos: valor en gramos
    """
    precio_convercion = precio * conversion / peso_gramos
    return precio_convercion