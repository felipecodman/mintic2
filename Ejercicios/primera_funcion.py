""" def imprime_Cosas():
  print("La clase esta genial")
  print('Python es lo máximo')
imprime_Cosas()

def repetir_funciones():
  print("\n")
  imprime_Cosas()
  imprime_Cosas()
repetir_funciones() """

""" def sumarDosnumeros():
  num1 = float(input("Ingrese el numero 1: "))
  num2 = float(input("Ingrese el numero 2: "))
  print("la suma de", int(num1), " + ", int(num2), " es igual a: ", int(num1 + num2))
sumarDosnumeros() """

""" def raizCuadrada():
  valor = float(input("Por favor, ntroduzca un numero a calcaluar su raiz cuadrada: "))
  raiz = valor ** 0.5
  return print("La raiz cuadrada de : ", valor, " es ", valor ** 0.5)
raizCuadrada() """

""" def mensaje():
  print("Ingrese por favor un valor")
def sumarDosnumeros():
  mensaje()
  num1 = float(input())
  mensaje()
  num2 = float(input())
  return print("la suma de ",num1, " + ", num2, " es igual a: ", num1 + num2)
sumarDosnumeros() """

""" def mensaje():
  print("Por favor, Introduzca un numero a calcaluar su raiz cuadrada: ")
def raizCuadrada():
  mensaje()
  valor = float(input())
  raiz = valor ** 0.5
  return print("La raiz cuadrada de : ", valor, " es ", valor ** 0.5)
raizCuadrada() """

""" def primeraFuncion(): # función externa
  print ("\n \"Hola desde la función externa\" \n ")
  def segundaFuncion(): # función interna
    print ("\n \"Hola desde la función interna\" \n")
  segundaFuncion()
primeraFuncion() """

""" def primerNumero(x):
  def segundoNumero(y):
    return x * y
  return segundoNumero
resultado = primerNumero(3)
print(resultado(5)) """

def primeraFuncion():
  x = 2
  def segundaFuncion(a):
    x = 6
    print(a + x)
  print(x)
  segundaFuncion(5)
primeraFuncion()