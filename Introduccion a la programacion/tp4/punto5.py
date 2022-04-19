"""
Lee dos números por teclado (una base y un exponente) y luego muestra en pantalla el resultado de elevar el número base a la
potencia exponente.
"""
base = int(input("Ingrese una Base que quiera calcular: "))
exponente = int(input("ingrese un Exponente que quiera calcular: "))
resultado = base ** exponente

print(f"El resultado de Elevar {base} por {exponente} es: {resultado}")