import random

def cargar_vector(vector_a,vector_b,cant):
    for i in range(cant):
        vector_a[i] = random.randint(1,1001)
        vector_b[i] = random.randint(1,1001)

def imprimir_vector(vector_1,vector_2,cant):
    print("Vector A:")
    for i in range(cant):
        print(vector_1[i], end=" ")
    print(" ")
    print("Vector B:")
    for i in range(cant):
        print(vector_2[i], end=" ")
    print(" ")

def sumatoria(vector_1,vector_2,cant):
    suma_impar = 0
    suma_par = 0
    for i in range(cant):
        if i %2==0:
            suma_par += vector_2[i]
        else:
            suma_impar += vector_1[i]
    suma_total = suma_par + suma_impar
    print("El resultado de sumar los elementos que ocupan las posiciones pares de la Lista A con las posiciones impares de la Lista B es:", suma_total)

cantidad = 120
vector_a = [0] * cantidad
vector_b = [0] * cantidad

cargar_vector(vector_a,vector_b,cantidad)
imprimir_vector(vector_a,vector_b,cantidad)
print(" ")
print(sumatoria(vector_a,vector_b,cantidad))