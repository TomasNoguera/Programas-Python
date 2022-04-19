def pedir_opcion():
    """
    Menu con 3 opciones, saludar, informar sobre la temperatura y mostrar el nombre de la materia.
    """
    try:
        print("********* MI PROGRAMA *********")
        print("1. Saludar.")
        print("2. Informar temperatura.")
        print("3. Mostrar nombre de materia.")
        
        opcion = int(input("Seleccione una opción [1-3]: "))
    
        if (opcion == 1):
            print("Hola, bienvenido a mi programa interactivo!")
        elif (opcion == 2):
            print("Hay una sensación térmica de 20 grados Celsius.")
        elif (opcion == 3):
            print("Estás en la materia Introducción a la Programación!")
    except ValueError:
        print("Solo puede ingresar un numero del 1 al 3")

pedir_opcion()