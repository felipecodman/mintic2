
""" lista = ["String", 10, 15.6, True] #list()

lista_cursos = ["Python", "Django", "Flask", "Ruby", "Java", "Rust"]
lista_cursos_2 = ["c", "c#"] """

""" primer_curso = lista_cursos[0]
print(primer_curso) """

""" lista_cursos[4] = "Rust"
print(lista_cursos) """

# [Start: end:skip] se puede obtener por saltos
""" sub_lista = lista_cursos[0:3] #No se tiene en cuenta el ultimo numero
print(sub_lista) """
""" print(len(lista_cursos)) #lo gandre que es la lista

lista_cursos.append("MongoDB") #Añadir al final de la lista
lista_cursos.insert(1, "Rails") #Añadir especificamente en un idice
lista_cursos.extend(lista_cursos_2) #Añadir una lista a otra

print(lista_cursos)
print(lista_cursos_2)

lista_cursos.remove("MongoDB") #Elimina con la palabras
del lista_cursos[1] #Elimina por posicion o indice

lista_cursos.clear() #Elimina toda una lista """

#print(lista_cursos)

from operator import index


lista = [10, 15, 4, 100, 20, 1, 8, 600, 3]



lista.sort() #Ordena los numeros de menor a mayor

print(min(lista)) # Sacar numero menor o mayor min ==max
print(max(lista))

lista.sort(reverse=True) #Ordena los numeros de mayor a menor
print(lista)
print(10 in lista) # para saber si hay un numero dentro del listado
print(10 not in lista) # Para no confirmar o negar el numero que esta en la lista, es decir si esta dira false

index = lista.index(10)
print(index)

print(lista[0]) # para imprimir los numero de acuerdo a su indice pero ordenados, es decir para saber por ejemplo el menor
print(lista[-1]) # o el mayor
