#Escribe un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por
# pantalla la paga que le corresponde.

print("*****Bienvenido usuario*****")

horas = float(input("Ingresar horas de trabajo: "))
costo_hora = float(input("Ingresar el costo por hora: "))

paga = horas * costo_hora

print("La paga es", "Q", paga)

print("*****************************") 