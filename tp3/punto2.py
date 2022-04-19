import random
from pyrecord import Record
import numpy as np

trabajadores = Record.create_type("Trabajador","nombre","edad","sexo","estado","salario",nombre="",edad=0,sexo="",estado="",salario=0)

def carga_aleatoria(v1):
	for i in range(len(v1)):
		v1[i] = trabajadores()
		v1[i].nombre = random.choice(nombres_trabajadores) #input(f"Ingrese el nombre del trabajador({i}): ")
		v1[i].edad = random.randint(18,65)
		v1[i].sexo = random.choice(genero_trabajadores)
		v1[i].estado = random.choice(estado_trabajadores)
		v1[i].salario = random.randint(15000,50000)

# Funciones para usar en random.choice y ahorrar tiempo
nombres_trabajadores = ['MARIA','EUGENIA','OSVALDO','JAVIER','TAMARA','AGUSTINA','MILAGROS',
		 'BELEN','VERONICA','ESTEFANIA','NAHUEL','ALEXANDER','NICOLAS',
		 'EZEQUIEL','ARIANA','ELIZABETH','DAIA','JORGE','MATIAS']
genero_trabajadores = ["F","M"]
estado_trabajadores = ["S","C","D","O"]

def mostrar_registro(v1):
	for i in range(len(v1)):
		# print(v1[i].nombre)
		# print(v1[i].edad)
		# print(v1[i].sexo)
		# print(v1[i].estado)
		# print(v1[i].salario)
		print("Nombre : ",v1[i].nombre," | Edad: ", v1[i].edad, " |","Sexo: ", v1[i].sexo," | Estado: ", v1[i].estado," | Salario: ",v1[i].salario)
		
def informacion_empleados(v1):
	cant_masculino = 0
	cant_casadas = 0
	empleado_joven = 100
	suma_salarios = 0
	
	for i in range(len(v1)):
		if v1[i].sexo == "M":
			cant_masculino += 1
		elif v1[i].sexo == "F" and v1[i].estado == "C":
			cant_casadas += 1
		
		if v1[i].edad < empleado_joven: # Sacar el menor numero de un registro, en este caso es el empleado mas joven
			empleado_joven = v1[i].edad

		suma_salarios += v1[i].salario
	print(f"Cantidad de trabajadores de sexo masculino: {cant_masculino}")
	print(f"Cantidad de trabajadoras casadas: {cant_casadas}")
	print(f"Empleado más joven: {empleado_joven}")
	print(f"Suma total de salarios: {suma_salarios}")

	
v1 = np.array([trabajadores]*5)

carga_aleatoria(v1)
mostrar_registro(v1)
print(" ")
print(informacion_empleados(v1))