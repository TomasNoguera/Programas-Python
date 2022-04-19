def notas_parcial():
    """
    Calcula la situación academica de un alumno ingresando las notas de dos parciales, puede ser promovido, regular o libre.
    """

    try:
        nota1 = int(input("Ingrese la nota del primer Parcial: "))
        nota2 = int(input("Ingrese la nota del segundo Parcial: "))

        promedio = (nota1 + nota2) /2

        if (nota1 < 10 ) or (nota1 > 0 ) or (nota2 < 10) or (nota2 > 0):
            print("Solo puede ingresar numeros enteros el 1 al 10")
        
        if (promedio >= 8) and (nota1 >= 4) and (nota2 >= 4):
            print(f"Su promedio es igual a {promedio}, lo que quiere decir que esta Promovido")

        elif (promedio <= 7) and (promedio >= 4) and (nota1 >= 4) and (nota2 >= 4):
            print(f"Su promedio es igual a {promedio}, lo que quiere decir que esta en condición de Regular")

        if (promedio <= 3) and (nota1 <= 4) and (nota2 <= 4):
            print(f"Su promedio es igual a {promedio}, lo que quiere decir que esta en condicion de Libre")

    except ValueError():
        print("Solo puede ingresar números enteros del 1 al 10.")

notas_parcial()