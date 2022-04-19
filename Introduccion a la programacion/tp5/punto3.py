def numeros_ingresados():
    """
    Solicita al usuario ingresar dos números por teclado y le indica por pantalla cuál de ellos es el mayor, si es igual o 0.
    """

    try:
        numero1 = int(input("Ingrese un número: "))
        numero2 = int(input("Ingrese un segundo número: "))


        if (numero1 > numero2):
            print(f"El número {numero1} es mayor que el número {numero2}")

        elif (numero1 < numero2):
            print(f"El número {numero2} es mayor que el número {numero1}")

        if (numero1 == numero2):
            print("Los dos números son iguales")
    except ValueError:
        print("Solo puede ingresar Números enteros")

numeros_ingresados()