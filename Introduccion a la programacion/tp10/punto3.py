def juego_nombres():
    cantidad = 10
    continuar = True
    while continuar:
        print("***** SUPER JUEGO TV *****")
        print(f"1. Comenzar ronda de {cantidad} nombres.")
        print("2. Salir.")
        opcion = input('Selecciona una opción [1-2]: ')
        if opcion == '1':
            for i in range(1, cantidad+1):
                    nombre = input(f'Ingrese el nombre número {i}: ')
                    if nombre != '':
                        print(f'El nombre "{nombre}" tiene {len(nombre)} caracteres.')
                    else:
                        print('No has ingresado ningún nombre, 0 caracteres.')

        elif opcion == '2':
            continuar = False
        else:
            print("Seleccione una opción válida.")

juego_nombres()