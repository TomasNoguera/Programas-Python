def compararlong(nombre1, nombre2):
    """
    Compara la cantidad de caracteres de dos strings
    """
    return len(nombre1) > len(nombre2)

nombretrue = str(input("Ingrese el primer nombre: "))
nombrefalse = str(input("Ingrese el segundo nombre: "))
print(compararlong(nombretrue,nombrefalse))