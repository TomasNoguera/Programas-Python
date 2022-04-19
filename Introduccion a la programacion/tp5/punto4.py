def numero_ingresado():
    """
    Solicita al usuario ingresar un número por teclado y le informa con un mensaje si su número es positivo, negativo, o 0.
    """
        
    try:
        numero = int(input("Ingrese un número: "))

    
        if (numero > 0 ):
            print(f"El número {numero} es Positivo")

        elif (numero < 0):
            print(f"El número {numero} es negativo")

        if (numero == 0):
            print("El número ingresado es igual a 0")
    except ValueError:
        print("Solo puede ingresar números enteros.")

numero_ingresado()