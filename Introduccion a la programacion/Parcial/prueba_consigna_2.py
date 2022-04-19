cantidad_emails = int(input(f"Ingrese la cantidad de emails enviados(1 de 100): "))
edad_ingresada = int(input("Ingrese su edad(1 de 10): "))
edad_mayor = 0

for i in range(1, 11):
    edad_ingresada = int(input(f"Ingrese un número ({i} de 10): "))
    if edad_ingresada > edad_mayor:
        edad_mayor = edad_ingresada
        edad_mayor = i
    
print(f"La edad de la persona que mas emails envia por dia es: ")
print()