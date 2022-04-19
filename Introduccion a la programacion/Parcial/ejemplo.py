def main(cantidad = 60):
    total_visitas = 0
    primer_ingreso = None
    primer_ingreso_repetido = False

    max_visitas = 0
    max_dominio = ""

    for universidad in range(cantidad):
        #Leo los ingresos y los dominios
        visitas, dominio = obtener_datos()
        #Sumar la cantidad a visitas al total
        #para luego calcular el promedio

        #Chequeo si el primer ingreso se repite
        if primer_ingreso is None:
            primer_ingreso = visitas
        elif visitas == primer_ingreso:
                primer_ingreso = True
        if visitas >= max_visitas:
            max_visitas = visitas
            max_dominio = dominio
    
    print(f"El promedio es {promedio}")
    if primer_ingreso_repetido:
        msg = "El primer ingreso se repite"
    else:
        msg = "El primer ingreso no se repite"
    print(msg)
    print(f"El Dominio mas visitado fue {max_dominio} con {max_visitas}")

if __name__ =="__main__":
    main(5)