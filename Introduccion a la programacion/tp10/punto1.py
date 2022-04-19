# Función que muestra en pantalla las opciones.
def mostrar_menu():
    print("************ DATOS PERSONALES ************")
    print("1. Mostrar datos actuales.")
    print("2. Actualizar nombre.")
    print("3. Actualizar apellido.")
    print("4. Actualizar correo electrónico.")
    print("5. Salir.")

def resolver_opcion_1(n, a, c):
    print('Los datos actuales son:')
    print(n)
    print(a)
    print(c)
    print('----------------------')

def resolver_opcion_2():
    nombre = input("Ingrese el nuevo valor para el nombre: ")
    return nombre

def resolver_opcion_3():
    apellido = input("ingrese el nuevo valor para el apellido: ")
    return apellido

def resolver_opcion_4():
    correo = input("ingrese el nuevo valor para el correo :")
    return correo

# Datos del usuario
nombre = "INDEFINIDO"
apellido = "INDEFINIDO"
correo = "INDEFINIDO"

continuar = True

# Mientras el usuario no elija  la opción salir
while continuar:
    mostrar_menu() #Mostrar el menu

    opcion = int(input("Ingrese una opción (1-5): "))

    while (opcion < 1 or opcion > 5): # Validar la opción
        print("La opción es invalida")
        opcion = int(input("Ingrese una opción (1-5): "))
    
    # Ejecutar la opción ingresada del usuario
    if (opcion == 1):
        resolver_opcion_1(nombre, apellido, correo)
    elif (opcion == 2):
        nombre = resolver_opcion_2()
    elif (opcion == 3):
        apellido = resolver_opcion_3()
    elif (opcion == 4):
        correo = resolver_opcion_4()
    else:
        continuar = False