mayor_cantidad_emails = 0
email_repetido = 0

for i in range(1, 6):
    cantidad_emails = int(input(f"Ingrese la cantidad de emails enviados({i} de 100): "))
    edad_ingresada = int(input(f"Ingrese su edad({i} de 100): "))   
        
    if (cantidad_emails > mayor_cantidad_emails):
        mayor_cantidad_emails = cantidad_emails
        edad_mayor = i
    elif cantidad_emails == cantidad_emails:
        email_repetido = i
        
    promedio_diario = cantidad_emails / 24
    
print(f"La edad de la persona que mas emails envia por dia es: {edad_mayor}")
print(f"El promedio de emails diarios es de: {promedio_diario:.2}")