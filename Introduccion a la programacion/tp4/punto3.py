"""
Muestra en pantalla el perímetro de un rectángulo, leyendo su base y altura desde teclado.
"""
base = int(input("Ingrese la Base del Rectangulo que desee calcular: "))
altura = int(input("Ingrese la Altura del Rectangulo que desee calcular: "))
perimetro = 2 * (base+altura)

print(f"El Perimero de un rectangulo con {base} de Base y {altura} de Altura es de: {perimetro} ")