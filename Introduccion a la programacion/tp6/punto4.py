def edad():
    """
    Solicita al usuario ingresar su edad y Verifica que el dato ingresado sea válido, teniendo en cuenta que la edad es 
    un número entero, y el rango es de 18 a 60 años.
    """
    try:
        edad_valida = int(input("Ingrese su edad: "))

        if (edad_valida >= 18) and (edad_valida <= 60):
            print("Su edad es: " +str(edad_valida))
        elif (edad_valida < 18) or (edad_valida > 60):
            print("Debe ingresar una edad entre 18 y 60.")
    except ValueError:
        print("El valor ingresado no es un número entero.")

edad()