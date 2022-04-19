def dia():
    """
    Ingresado un número del día de la semana ingresado por teclado, muestra el nombre de ese día en lenguaje natural.
    """
    try:
        numero = int(input("Ingrese un número del 1 al 7: "))

        if numero == 1:
            print("El dia de la semana elegido es Domingo.")
        elif numero == 2: 
            print("El dia de la semana elegido es Lunes.")
        elif numero == 3:
            print("El dia de la semana elegido es Martes.")
        elif numero == 4:
            print("El dia de la semana elegido es Miercoles.")
        elif numero == 5:
            print("El dia de la semana elegido es Jueves.")
        elif numero == 6:
            print("El dia de la semana elegido es Viernes.")
        elif numero == 7:
            print("El dia de la semana elegido es Sabado.")
        else:
            print("Solo puede ingresar un número entre 1 y 7.")
    except ValueError:
        print("Error, Solo puede ingresar números enteros entre 1 y 7.")

dia()