import random

filas = 3
columnas = 3
matriz = [[0] * columnas for i in range(filas)]

def carga_aleatoria(matriz,filas,columnas):
    for f in range(filas):
        for c in range(columnas):
            matriz[f][c] = random.randint(1,51)

def mostrar_matriz(matriz,filas,columnas):
    for f in range(filas):
        for c in range(columnas):
            print(matriz[f][c], end=" ")
        print("")

def permutacion(matriz,filas,columnas):
    for f in range(filas):
        contador = 0
        for c in range(columnas):
            if (c < columnas):
                contador = contador + matriz[c][f]
                aux = matriz[f][c]
                matriz[f][c] = matriz[c][f]
                matriz[c][f] = aux
        return matriz

# Carga
carga_aleatoria(matriz,filas,columnas)

# Mustra
print("Matriz Original:")
mostrar_matriz(matriz,filas,columnas)

# Permutacion
print("Matriz Permutada:")
matriz = permutacion(matriz,filas,columnas)
mostrar_matriz(matriz,filas,columnas)