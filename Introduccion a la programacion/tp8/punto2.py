"""
Muestra sólo los números pares entre los primeros 100 números enteros positivos, comenzando desde el 1.
"""

for numeros_pares in range(1, 101):
    if numeros_pares % 2 == 0:
        print(numeros_pares)