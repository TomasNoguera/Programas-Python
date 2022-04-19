numero_mayor = 1
numero_menor = 1
for i in range(2, 11):
    numero_ingresado = int(input("Ingrese un número: "))
    if numero_ingresado > numero_mayor:
        numero_mayor = numero_ingresado
        posicion_mayor = i
    if numero_ingresado < numero_menor:
        numero_menor = numero_ingresado
        posicion_menor = i

print("El mayor número es ", numero_mayor, "y lo ingresaste en la posición ", posicion_mayor)
print("El menor número es ", numero_menor, "y lo ingresaste en la posición ", posicion_menor)