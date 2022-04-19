def usuario(numeroletras):

    """
    Solicita ingresar un nombre de usuario y luego muestra en pantalla cuántas letras tiene ese nombre.
    """

    contarletras = len(numeroletras)
    return contarletras

nombreusuario = str(input("Ingrese su nombre de usuario: "))
print(usuario(nombreusuario))