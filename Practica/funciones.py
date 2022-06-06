""" def saludar (nombre):
  return f"Hola {nombre} bienvenido"

print("Ingresa tu nombre")
nombre = input()
print(saludar(nombre)) """

def salaryweek(hrs, salaryHr, job):
  salary = hrs * salaryHr
  salary = salary * 7
  print("El sueldo de un", job, "es:",salary)
salaryweek(8, 284, "Doctor")
salaryweek(4, 10, "Jardinero")