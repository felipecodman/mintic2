""" def ejercicio_3 (n):
  tmp = 1
  for i in range(n):
    tmp *= i + 1
    return tmp
print(ejercicio_3(5))
print(ejercicio_3(20)) """

def MensajeBienvenida():
  print("Buenas tarde para todos los tripulantes");
  print("Espero que esten aprendiendo 2022");
  print("Millones de exitos");

#MensajeBienvenida();

""" def SumarDosNumeros(Numero1, Numero2):
  Suma = Numero1 + Numero2
  return f"El resultado de la suma es: {Suma}" """

def CalculadoraDeSuma():
  Numero1 = int(input("Por favor, ingrese un numero: "))
  Numero2 = int(input("Por favor, ingrese un numero: "))
  return f"El resultado de la suma es: {Numero1 + Numero2}"

