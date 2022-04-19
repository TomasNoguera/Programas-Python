# Dado un arreglo de N elementos de tipo entero y un número X ingresado
# por teclado, escribir un función que:
# a. Busque todos los elementos que coincidan con X y devuelva la
# cantidad de coincidencias encontradas.
# b. Busque la primera coincidencia del elemento en la lista y devuelva
# su posición. Si X no existe en el arreglo debe devolver -1.
# c. Utilizando la función anterior, busque todos los elementos que
# coincidan con X y devuelva un arreglo con las posiciones que
# ocupan estos elementos en el arreglo original. Si no hay elementos
# coincidentes, devolverá un arreglo vacío.

import random
import os

Na = 12
arreglo = [0 for y in range(Na)]
Nf = 12
pos_arreglo = [0]*Nf
Np = 12
posiciones = [0]*Np

# Programas Accesorios:

def carga_vector(v):
    for i in range (len(v)):
        v[i] = random.randint(1,9)

def muestra_vector(v):
    for i in range (len(v)):
        print(v[i], end= " ")
    print()


def busca_valor(v,x):
    veces = 0
    i = 0
    primera_pos = -1
    while i < len(v):
        if v[i] == x:
            veces = veces + 1
            pos_arreglo[i] = 1
            posiciones[i] = i + 1
        i = i + 1

    i = 0
    while primera_pos == -1 and i < (len(pos_arreglo)):
        if pos_arreglo[i] == 1:
            primera_pos = i + 1
            
        i = i + 1
    return x,veces,primera_pos,posiciones


    
def pausa():
    print()
    input("Presione Enter para Continuar.")
    os.system("cls")


# Programa Principal:

print()
opcion = 100
os.system("cls")


while opcion != 0:
    print()	
    print("******.   MENU.  *******")
    print(" 1. Cargar arreglo aleatoriamente con #s entre 1 y 9.")
    print(" 2. Mostrar mostrar arreglo.")
    print(" 3. Buscar dato en el arreglo, mostrar frecuencia y posiciones.")
    print(" 0. Salir.")
    print()

    opcion = int(input("Ingrese una opción, por favor: "))
    os.system("cls")

    if opcion == 1:
        carga_vector(arreglo)
        print("El vector fue cargado satisfactoriamente.")
        print()
        pausa()
    elif opcion == 2:
        print("El vector cargado es: ")
        print()
        muestra_vector(arreglo)
        print()
        pausa()
    elif opcion == 3:
        print()
        #encontrar = input("Ingrese el apellido que desea encontrar: ")
        print()
        buscado = int(input("Ingrese el elemento a encontrar en el arreglo: "))
        x,veces,primera_pos,posiciones=busca_valor(arreglo,buscado)
        print()
        muestra_vector(arreglo)
        print()
        print("El elemento",x,"se encuentra en el vector: ", veces,"veces.")
        print()
        print("La primera posición que ocupa en el vector es: ", primera_pos,".")
        print()
        print("Las posiciones ocupadas en todo el vector son: ", posiciones,".")
        pausa()
        posiciones = [0]*Np
        pos_arreglo = [0]*Nf
    elif opcion == 0:
        print()
        print("Hasta Pronto.")
        pausa()
    else:
        print()
        input("Opción Inválida. Presione Enter para continuar.")
        pausa()