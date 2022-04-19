import os
opcion = -1
opcion_ingresada = 0

while opcion_ingresada <= 1 or opcion_ingresada >= 4:
    
    try:
        
        print("********* MI PROGRAMA *********")
        print("1. Saludar.")
        print("2. Informar temperatura.")
        print("3. Mostrar nombre de materia.")
        print("4. Salir")
        
        opcion_ingresada = int(input("Seleccione una apcion [1-4]: "))

        if (opcion_ingresada == 1):
            print("Hola, bienvenido a mi programa interactivo!")
            input("[PRESIONE ENTER PARA CONTINUAR]")
            os.system("cls")
        elif (opcion_ingresada == 2):
            print("Hay una sensación térmica de 20 grados Celsius.")
            input("[PRESIONE ENTER PARA CONTINUAR]")
            os.system("cls")
        elif (opcion_ingresada == 3):
            print("Estás en la materia Introducción a la Programación!")
            input("[PRESIONE ENTER PARA CONTINUAR]")
            os.system("cls")
        else:
            print("Gracias por usar el Menu.")
            input("[PRESIONE ENTER PARA CONTINUAR]")
            os.system("cls")
    except ValueError:
        print("Solo puede ingresar un numero del 1 al 4")