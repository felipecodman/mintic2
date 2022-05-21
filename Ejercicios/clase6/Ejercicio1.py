from asyncio.windows_utils import pipe
def validacion_nota(nota: float) -> str:

#Validar parametros
#nota < 0.0 or nota > 5.0:

  if not(nota >= 0.0 and nota <= 5.0):
    return "ingrese un valor entre 0.0 y 5.0"

#Proceso
  mensaje = ""
  if nota >= 4.0:
    mensaje="!Felicitaciones!"

#salida

  return f"Su nota es {nota}{mensaje}"
