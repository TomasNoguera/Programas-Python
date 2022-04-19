def temperatura():
    """
    Solicita al usuario ingresar una temperatura en grados Celsius y valida que la entrada sea correcta teniendo en cuenta que la 
    temperatura debe ser un número real (flotante) y el rango válido está entre -18 y 50.
    """
    
    try:
        celsius = float(input("Ingrese la temperatura en Grados Celsius: "))
    
        if(celsius >= -18) and (celsius <= 50):
            print("La Temperatura ingresada es: " +str(celsius))
        elif (celsius < -18) or (celsius > 50):
            print("La Temperatura ingresada debe ser entre -18 y 50 grados Celsius.")
    except ValueError:
        print("El valor ingresado no es un número Real.")

temperatura()