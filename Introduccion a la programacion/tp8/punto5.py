"""
Solicita al usuario ingresar 10 números enteros, y por cada uno, le informa si el mismo es positivo, negativo, o cero.
"""

numero_menor = 0
numero_mayor = 0
numero_igual = 0
for i in range(1, 11):
    numero_ingresado = int(input(f"Ingrese 10 números enteros({i} de 10): "))
    if numero_ingresado > numero_mayor:
        numero_ingresado = print("El numero ",numero_ingresado,"es  Positivo")
    elif numero_ingresado < numero_menor:
        numero_ingresado = print("El número ",numero_ingresado,"es Negativo")
    if numero_ingresado == numero_igual:
        numero_ingresado = print("El número ",numero_ingresado,"es igual a 0")