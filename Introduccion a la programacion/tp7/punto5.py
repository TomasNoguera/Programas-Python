def mayuscula(palabra): # Hacer que retorne una palabra en Mayuscula
    
    """
    Recibe un string como parámetro y retorna el mismo string pero con todas las letras convertidas a mayúsculas.
    """
    
    return palabra.upper() #variable.upper hace que la palabra se ponga en Mayuscula print(mayus())

palabra = input("Ingrese una Palabra: ")
palabramayuscula = mayuscula(palabra)

print(palabramayuscula)