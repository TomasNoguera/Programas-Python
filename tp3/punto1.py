import random
from pyrecord import Record
import numpy as np

notas = Record.create_type("Nota","alumno","legajo","nota1","nota2","nota3",alumno ="",legajo = 0,nota1 = 0,nota2 = 0,nota3= 0)

def carga_aleatoria(v1):
	for i in range(len(v1)):
		v1[i] = notas()
		v1[i].alumno = input(f"Ingrese un Apellido({i}): ")
		v1[i].legajo = random.randint(1,100)
		v1[i].nota1 = random.randint(1,10)
		v1[i].nota3 = random.randint(1,10)
		v1[i].nota2 = random.randint(1,10)

#def mostrar_registro(v1):
	#for i in range(len(v1)):
		# print(v1[i].alumno)
		# print(v1[i].legajo)
		# print(v1[i].nota1)
		# print(v1[i].nota2)
		# print(v1[i].nota3)
		# print(v1[i].condicion)
		#print("Nombre : ",v1[i].alumno," | Legajo: ", v1[i].legajo, " |","Promedio: ", v1[i].promedio," | Condicion: ", v1[i].condicion)

def condicion_alumno(v1):
	for i in range(len(v1)):
		promedio = (v1[i].nota1 + v1[i].nota2 + v1[i].nota3) / 3
		if promedio < 4:
			condicion = "Libre"
		elif promedio >= 4 and promedio <= 6:
			condicion = "Regular"
		elif promedio >= 7:
			condicion = "Promovido"
		print(f"Nombre : {v1[i].alumno} | Legajo: {v1[i].legajo} | Promedio: {promedio} | Condicion: {condicion}")

v1 = np.array([notas]*10)

carga_aleatoria(v1)
print(condicion_alumno(v1))