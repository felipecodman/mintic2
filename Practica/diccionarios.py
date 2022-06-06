from typing import Tuple


elementos = {'a': 1, 'b': 2, 'c': 3, 'd':4}

""" elementos['nombre'] = 'Cody' #Crea la llave con su valor
elementos[(1, 2, 3)] = 'La llave es una tupla'

elementos['nombre'] = 'mintic' #Actualiza el valor de la llave
 """
""" print(elementos)
print(len(elementos)) """

#print('z' in elementos)
""" valor = elementos ['d']
print(valor) """

# Get
# setdefault > return si no existe la añade

""" valor = elementos.setdefault('z', 5)
print(valor)
print(elementos) """

# Keys
# Values
# items

""" llaves = tuple(elementos.keys())
print(llaves)

valores = tuple(elementos.values())
print(valores)

diccionarios = tuple(elementos.items())
print(diccionarios) """

print(len(elementos))

del elementos['a'] #1
valor = elementos.pop('b') #2

elementos.clear()

print(valor)

print(elementos)
print(len(elementos))
