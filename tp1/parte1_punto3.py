lista = [1,2,3,4,5]
print("Lista original:", lista)

primera_posicion = 5
x = primera_posicion

for i in range(len(lista)):
    if(lista[i] == x):
        lista = [lista[i]] + lista[:i] + lista[i + 1:]
print("Nueva lista:   ", lista)

# def desplazar(vector):
#         modulo = len(vector)
#         vector_aux = [0]*modulo
#         for i in range(modulo):
#             vector_aux[(i+1)%modulo] = vector[(i)%modulo]
#         return vector_aux