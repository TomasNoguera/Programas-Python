import random

vec1 = [0] * 5

def cargar_vector(vector):
    for i in range(len(vector)):
        vector[i] = random.randint(-100,100)

def mostrar_vector(vector):
    for i in range(len(vector)):
        print(vector[i], end=" | ")

def calcular_numeros():
    positivos = 0
    negativos = 0
    ceros = 0

    for i in range(vec1):
        if vec1[i] >= 1:
            positivos += 1
        
        elif vec1[i] <= -1:
            negativos += 1
        
        else:
            ceros += 1
    return positivos,negativos,ceros

opcion = 100

while opcion != 4:
	print()	
	print("******.   MENU.  *******")
	print(" 1. Generar el vector")
	print(" 2. Mostrar el vector")
	print(" 3. Calcular la cantidad de Positivos, Negativos y Ceros")
	print(" 4. Salir.")
	
	opcion = int(input("Ingrese una opción, por favor: "))
	
	if opcion == 1:
		cargar_vector(vec1)
		input("El vector ha sido cargado correctamente. Presione Enter para continuar.")
	elif opcion == 2:
		mostrar_vector(vec1)
		print()
		continuar = input("Presione Enter para continuar.")
	elif opcion == 3:
		print()
		print(calcular_numeros(vec1))
		print()
		continuar = input("Presione Enter para continuar.")
	elif opcion == 4:
		print()
		print("Hasta Pronto.")
	else:
		print()
		input("Opción Inválida. Presione Enter para continuar.")