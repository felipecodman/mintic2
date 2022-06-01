""" Suma = 0
cantidadNumeros = int(input("Por favor, ingrese la cantidad de numeros"));
for n in range(cantidadNumeros):
   Numero=int(input("Ingrese un numero:"));
   #Suma=Suma+Numero;
   Suma+= Numero;

print("El resultado de la suma es:", Suma) """

""" from taller import SumarDosNumeros
print (SumarDosNumeros(5, 5))
print (SumarDosNumeros(Numero1=10, Numero2=10)) """

from taller import CalculadoraDeSuma

print (CalculadoraDeSuma())
