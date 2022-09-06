""" numbers = [1,2,3,4,5]
print(numbers[2])

Colores = ["Verde", "Morado", "Amarillo"]
person = {"name":"Marines","lastname":"Mendez","age":24}

print(Colores.pop(2)) #nos devuelve un elemeto y luego lo borra/*

for value in Colores:
  print(value)
# print(person.get("name"))
for key, value in person.items():
  print(key," ",value) 
"""

""" def plusNumbers (list):
  even= 0
  odd = 0
  for value in list:
    if value % 2 == 0:
      even = even + value
    else:
      odd = odd +value
  print("Suma de numeros pares",even)
  print("Suma de numero impares", odd)
  
  
plusNumbers([1, 2, 3, 4, 5, 6, 7]) """
""" 
shoes = [
  {"Nike":"tenis1", "Converse": "tenis2", "Adidas": "tenis3"},
  {"Nike":"tenis4", "Converse": "tenis5", "Adidas": "tenis6"},
  {"Nike":"tenis7", "Converse": "tenis8", "Adidas": "tenis9"}]

print(shoes[2]["Adidas"]) """

matrix1 = [[1, 2, 3],[7, 8, 9], [13, 14, 15]]
matrix2 = [[4, 5, 6],[10, 11, 12], [16, 17, 18]]

matrix3 = [[1, 2, 3], [7, 8, 9], [13, 14, 15]]
matrix3[0][0]= matrix1[0][0] + matrix2[0][0]

for rowPosition, value in enumerate(matrix1):
  for columPosition, value2 in enumerate(value):
    matrix3[rowPosition][columPosition]= value2 + matrix2[rowPosition][columPosition]
print(matrix3)
