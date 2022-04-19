def lados():
    """
    Determina si un triángulo es isósceles, equilátero, o escaleno ingresando tres numeros.
    """
    try:
        numero1 = int(input("Ingrese el primer Lado que desea cálcular: "))
        numero2 = int(input("Ingrese el segundo Lado que desea cálcular: "))
        numero3 = int(input("Ingrese el tercer Lado que desea cálcular: "))

        if(numero1 == numero2 == numero3):
            print("El Triangulo ingresado es Equilátero.")

        elif(numero1 == numero2) or (numero1 == numero3) or (numero2 == numero3):
            print("EL Triangulo ingresado es Isósceles.")

        if(numero1 % numero2 % numero3): # % Se usa para cuando queres que los input sean diferentes.
            print("El Triangulo ingresado es Escaleno.")
    except ValueError():
        print("Solo puede ingresar números enteros.")

lados()