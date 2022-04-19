"""
Solicita al usuario ingresar un número entero y muestra en pantalla el factorial de dicho número.
"""

numero_entero = int(input("Ingrese un Número entero: "))

while numero_entero < 1:
    numero_entero = int(input("Ingrese un Número entero positivo: "))
factorial = 1

for numero_ingresado in range(1, numero_entero + 1):
    factorial = factorial * numero_ingresado

print("El Factorial de ", numero_entero, "es ", factorial)