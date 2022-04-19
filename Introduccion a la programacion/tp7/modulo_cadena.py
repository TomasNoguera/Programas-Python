def leer_cadena():
    """
    sin recibir ningún parámetro, le solicita al usuario leer un string cualquiera y luego lo retorna.
    """
    x = input("Ingrese una palabra: ")
    return x

x = leer_cadena()
print(x)