"""
Solicita al usuario ingresar 10 números y muestra en pantalla cuál de ellos es el máximo, y en qué posición lo ingresó.
"""

numero_mayor = 0

for i in range(1, 11):
    numero_ingresado = int(input(f"Ingrese un número ({i} de 10): "))
    if numero_ingresado > numero_mayor:
        numero_mayor = numero_ingresado
        posicion_mayor = i
    
print("El mayor número es ", numero_mayor, "y lo ingresaste en la posición ", posicion_mayor)