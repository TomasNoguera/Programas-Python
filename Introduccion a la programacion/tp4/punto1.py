"""
Solicita al usuario ingresar su nombre de pila, luego lo saluda y calcula la cantidad de letras de su nombre.
"""
nombre = input("Ingrese su nombre: ") # Calcula la cantidad de letras de tu Nombre
numeroletras = len(nombre)

print("Hola, "+nombre+", tu nombre tiene "+str(numeroletras)+" letras.")