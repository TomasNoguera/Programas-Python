def numero_ingresado():
    """
    Solicita al usuario ingresar un número por teclado y luego le informa en pantalla si su número es mayor que 10.
    """
    try:
        numero = int(input("Ingrese un número: "))

        if (numero > 10):
            print(f"Tu número {numero} es mayor que 10")
            print("Saludos!") 

        elif (numero <= 10):
            print("Saludos!")
    except ValueError:
        print("Solo puede ingresar Números enteros.")

numero_ingresado()