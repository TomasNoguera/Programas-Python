suma= 0
cantidad_intentos= 0
notas_ingresadas= 0

while (notas_ingresadas != -1):
    notas_ingresadas = input("ingrese la nota del parcial: ")
    try:
        notas = int(notas_ingresadas)
        if (notas >= 1 and notas <= 10):
            suma = notas+suma
            cantidad_intentos = cantidad_intentos + 1
        elif (notas == -1):
            break
        else:
            print("Número fuera de rango")
    except:
        print("El dato ingresado no es un numero entero.")


promedio = (suma/cantidad_intentos)

print(promedio)