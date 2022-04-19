import random

filas = 3
columnas = 3
matriz = [[0] * columnas for i in range(filas)]

vector_filas = 0
vector_columnas = 0

def carga_aleatoria(matriz,filas,columnas):
    for f in range(filas):
        for c in range(columnas):
            matriz[f][c] = random.randint(0,9)

def mostrar_matriz(matriz,filas,columnas):
    for f in range(filas):
        for c in range(columnas):
            print(matriz[f][c], end=" ")
        print("")

def suma_filas_columnas(matriz,filas,columnas,vector_filas,vector_columnas):
    for f in range(filas):
        contador = 0
        for c in range(columnas):
            contador = contador + (matriz[f][c])
            vector_columnas = vector_columnas + matriz[f][c]
        vector_filas = contador
        print("La suma de la fila de la matriz es:", vector_filas)
        print("La suma de la columna de la matriz es:", vector_columnas)

# Carga
carga_aleatoria(matriz,filas,columnas)

# Mustra
mostrar_matriz(matriz,filas,columnas)

# Suma
suma_filas_columnas(matriz,filas,columnas,vector_filas,vector_columnas)