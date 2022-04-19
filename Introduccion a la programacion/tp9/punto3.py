numero = -1
valido = False

while not valido:
    numero = input("Ingrse un número entre 1 y 100: ")
    
    if numero.isdigit():
        numero = int(numero)
        if numero >= 1 and numero <= 100:
            valido = True
            print(numero," es valido, gracias!")
        else:
            print("El número ingresado esta fuera del rango permitido.")     
    else:
        print("El dato ingresado no es númerico.")