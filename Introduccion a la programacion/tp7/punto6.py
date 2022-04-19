def minuscula_mayuscula(palabra):

    """
    Recibe un string como parámetro y retorna dos versiones del string recibido como parámetro, primero en minúsculas y 
    luego en mayúsculas
    """
    minus = palabra.lower()
    mayus = palabra.upper()
    return minus, mayus



palabra = input("Ingrese una Palabra: ")
palabraminuscula, palabramayuscula = minuscula_mayuscula(palabra)

print("En minuscula, su palabra es: ",palabraminuscula)
print("En mayuscula, su palabra es: ",palabramayuscula)