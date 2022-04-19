"""
Muestra notas de los parciales ingresando el Apellido del Alumno.
"""

nombre = input("Ingrese su Apellido: ")
nota1 = 8
nota2 = 6
promedio = (nota1+nota2) / 2

print("Alumno "+str(nombre))
print("Primer Parcial: "+str(nota1))
print("Segundo Parcial: "+str(nota2))
print("Promedio: "+str(promedio))