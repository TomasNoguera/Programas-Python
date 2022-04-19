import random

escalar_producto = 0

lista_a = [0] * 10
for i in range(10):
    lista_a[i] = random.randint(0,12)

lista_b = [0] * 10
for i in range(10):
    lista_b[i] = random.randint(0,12)

print("Lista A:", lista_a)
print("Lista B:", lista_b)

for i in range(0,10):
    escalar_producto = escalar_producto + lista_a[i] * lista_b[i]

print("El producto de escalar los dos vectores es:", escalar_producto)