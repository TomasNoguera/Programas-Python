def parcial():

    try:
        nota = int(input("Ingrese una nota de parcial (1-10): "))
        print("La nota ingresada es " + str(nota))
        
        if (nota > 10):
            print("Solo puede ingresar una nota del 1 al 10.")
        elif (nota < 1):
            print("Solo puede ingresar una nota del 1 al 10.")
    except ValueError:
        print("El valor ingresado no es un número entero.")

parcial()