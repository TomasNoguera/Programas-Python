# Realizar un algoritmo que permita cargar dos arreglos de n elementos:
# Apellido (n) y Nombre(n). Ordenarlos en forma ascendente y generar un
# listado.

# Programas Accesorios:

def carga_nombres_apellidos(v_nombres,v_apellidos):
    print()
    print("A continuación deberá ingresar 3 nombres y 3 apellidos.")
    print()
    for i in range (len(v_nombres)):
        v_nombres[i] = input("Ingrese un nombre, por favor: ")
        print()
        v_apellidos[i] = input("Ingrese un apellido, por favor: ")
        print()
        pausa()
    print()
    

def ordena_nombres_por_apellidos(v_apellidos,v_nombres):
    se_cambio = True
    while se_cambio:
        se_cambio = False
        i = 1
        while i < len(v_apellidos):
            if v_apellidos[i-1] > v_apellidos[i]:
                aux_a = v_apellidos[i-1]
                aux_n = v_nombres[i-1]
                v_apellidos[i-1] = v_apellidos[i]
                v_apellidos[i] = aux_a
                v_nombres[i-1] = v_nombres[i]
                v_nombres[i] = aux_n

                se_cambio = True

            i = i + 1

    return v_apellidos,v_nombres

def muestra(v_apellidos,v_nombres):
    print()
    print("APELLIDO:     NOMBRE:")
    print()
    for i in range (len(v_apellidos)):
        print(v_apellidos[i], " "*5,v_nombres[i])
        print()
        
def pausa():
    print()
    input("Presione Enter para Continuar.")
    os.system("cls")


# Programa Principal:

import numpy as np
import os

nombres = np.array([" "*15]*3)
apellidos = np.array([" "*15]*3)

print()
opcion = 100
os.system("cls")

while opcion != 0:
    print()	
    print("******.   MENU.  *******")
    print(" 1. Cargar nombres y apellidos.")
    print(" 2. Mostrar mostrar datos.")
    print(" 3. Ordenar datos.")
    print(" 0. Salir.")
    print()

    opcion = int(input("Ingrese una opción, por favor: "))
    os.system("cls")

    if opcion == 1:
        carga_nombres_apellidos(nombres,apellidos)
        print("El vector fue cargado satisfactoriamente.")
        print()
        pausa()
    elif opcion == 2:
        print("El vector cargado es: ")
        print()
        muestra(apellidos,nombres)
        print()
        pausa()
    elif opcion == 3:
        print()
        print()
        ordena_nombres_por_apellidos(apellidos,nombres)
        print()
        print("Los Datos han sido ordenados por apellidos correctamente.")
        pausa()
    elif opcion == 0:
        print()
        print("Hasta Pronto.")
        pausa()
    else:
        print()
        input("Opción Inválida. Presione Enter para continuar.")
        pausa()