"""
Solicita al usuario ingresar 10 números y muestra en pantalla cuál de ellos es el máximo, minimo, igual a cero 
y en qué posición se ingresaron dichos números.
"""

numero_mayor = int(input("Ingrese un número(1 de 10): "))
posicion_mayor = 1
posicion_menor = 1
# Tomamos como número mayor y menor al primer número ingresado
numero_menor = numero_mayor 
# Cambiamos el range a 2,11 porque el primer valor se ingresa fuera del for.
for i in range (2,11):
    numero_ingresado = int(input(f"Ingrese un número({i} de 10): "))
    if numero_ingresado > numero_mayor:
        numero_mayor = numero_ingresado
        posicion_mayor = i
    elif numero_ingresado < numero_menor:
        numero_menor = numero_ingresado
        posicion_menor = i
        
print("El mayor número ingresado es ", numero_mayor," y lo ingresaste en la posición ",posicion_mayor)
print("El menor número ingresado es ", numero_menor," y lo ingresaste en la posición ",posicion_menor)