suma= 0
cantidad_intentos= 0
numero_ingresado= 0 # = notas_ingresadas

while (numero_ingresado != -1):
    numero_ingresado = input("ingrese un numero entero: ")
    try:
        numero_valido = int(notas_ingresadas)
        if (numero_valido >= 1 and numero_valido <= 10):
            print(numero_valido," es valido, gracias!")
        elif (numero_valido < -1):
            print("Número fuera de rango")
    except:
        print("El dato ingresado no es un numero entero.")
