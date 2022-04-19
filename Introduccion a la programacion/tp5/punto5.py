def dias_semana():
    """
    Ingresado un número del día de la semana ingresado por teclado, muestra el nombre de ese día en lenguaje natural.
    """
    try:
        dia = int(input("Ingrese un dia de la semana: "))

        if (dia == 1):
            print("El dia de la semana elegido es Domingo")

        if (dia == 2):
            print("El dia de la semana elegido es Lunes")

        if (dia == 3):
            print("El dia de la semana elegido es Martes")

        if (dia == 4):
            print("El dia de la semana elegido es Miercoles")

        if (dia == 5):
            print("El dia de la semana elegido es Jueves")

        if (dia == 6):
            print("El dia de la semana elegido es Viernes")

        if (dia == 7):
            print("El dia de la semana elegido es Sabado")
    except ValueError:
        print("Solo puede ingresar números del 1 al 7.")

dias_semana()