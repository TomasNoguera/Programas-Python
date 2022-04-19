import random

def cargar_vector(arreglo,cant):
	for i in range(cant):
		arreglo[i] = random.randrange(1000)

def mostrar_vector(arreglo,cant):
	for i in range(cant):
		print(arreglo[i], end=" - ")

def ordenar_insercion(vector,elementos):
	orden = input("Ingrese el orden que desea usar para los elementos del Vector(A/D): ")
	if orden == "A":
		for i in range(1,elementos):
			j = i
			while (j > 0) and (vector[j - 1] > vector[j]):
				#realizamos el itercambio
				swap = vector[j - 1]
				vector[j - 1] = vector[j]
				vector[j] = swap
				j = j - 1
	
	if orden == "D":
		for i in range(1,elementos):
			j = i
			while (j > 0) and (vector[j - 1] < vector[j]):
				#realizamos el itercambio
				swap = vector[j - 1]
				vector[j - 1] = vector[j]
				vector[j] = swap
				j = j - 1
	return vector

cantidad = 20
vector = [0] * cantidad
opcion = 100

while opcion != 3:
	print()
	print("******.   MENU.  *******")
	print(" 1. Generar el vector ")
	print(" 2. Mostrar el vector ")
	print(" 3. Ordenar el vector(A/D) ")
	
	opcion = int(input("Ingrese una opción, por favor: "))

	if opcion == 1:
		cargar_vector(vector,cantidad)
		input("El vector ha sido cargado correctamente. Presione Enter para continuar.")
	elif opcion == 2:
		mostrar_vector(vector,cantidad)
		print()
		continuar = input("Presione Enter para continuar.")
	elif opcion == 3:
		print()
		print(ordenar_insercion(vector,cantidad))
		print()
		continuar = input("Presione Enter para continuar.")
		print("Hasta Pronto.")
	else:
		print()
		input("Opción Inválida. Presione Enter para continuar.")

# Ejemplo sin menu
# cargar_vector(vector,cantidad)
# mostrar_vector(vector,cantidad)
# print(ordenar_insercion(vector,cantidad))