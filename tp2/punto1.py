import random

filas = 3
columnas = 4
matriz = [[0] * columnas for i in range(filas)]

def carga_aleatoria(matriz,filas,columnas):
    for f in range(filas):
        for c in range(columnas):
            matriz[f][c] = random.randint(0,9)

def mostrar_matriz(matriz,filas,columnas):
    for f in range(filas):
        for c in range(columnas):
            print(matriz[f][c], end=" ")
        print("")

def suma_matriz(matriz,filas,columnas):
    suma = 0
    for f in range(filas):
        for c in range(columnas):
            suma = suma + (matriz[f][c])
    print("La suma de la matriz es:", suma)

# Carga
carga_aleatoria(matriz,filas,columnas)

# Mustra
mostrar_matriz(matriz,filas,columnas)

# Suma
suma_matriz(matriz,filas,columnas)