def nota_valida(nota):
    #ret = False
    nota = str(nota)
    return nota.isdigit() and int(nota) >= 0 and int(nota) <= 10
        #ret = True
    #else:
       #ret = False
    #return ret

def obtener_promedio():
    suma = 0
    cantidad = 0
    mas_notas = True

    while mas_notas: 
        nota = input("Ingrese la nota (1 a 10, o -1 para terminar):")

        if nota_valida(nota):
            cantidad += 1
            suma += int(nota)
        elif nota == "-1":
            mas_notas = False
        else:
            print("Nota invalida.")
    if cantidad > 0:
        ret = suma/cantidad
    return ret
    
if __name__ == "__main__":
    promedio_1 = obtener_promedio()
    print(f"El promedio de la comision 1 es {promedio_1}")
    promedio_2 = obtener_promedio()
    print(f"El promedio de la comision 2 es {promedio_2}")

    if promedio_1 > promedio_2:
        print("El promedio de la comision 1 es mayor al de la comision 2.")
    elif promedio_2 > promedio_1:
        print("El promedio de la comision 2 es mayor al de la comision 1.")
    else:
        print("Las comisiones tienen el mismo promedio.")