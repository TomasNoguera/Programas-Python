def color_favorito():
    """
    solicite al usuario ingresar cuál es su color favorito, limitando las opciones a rojo, verde, y azul.
    """
    try:
        color = str(input("Ingrese su color favorito entre Rojo, Verde y Azul: "))
        if (color == "rojo"):
            print("Su Color favorito es Rojo")
        elif (color == "verde"):
            print("Su Color favorito es Verde")
        elif (color == "azul"):
            print("Su Color favorito es Azul")
    except ValueError:
        print("Solo puede ingresar un color entre Rojo, Verde y Azul")

color_favorito()