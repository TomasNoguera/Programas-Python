maximo = -1
posicion_maximo = None

minimo = 9999
posicion_minimo = None

primer_numero = None
cantidad_primer_numero = 0

for n in range(1, 10):

    numero = int(input("Ingrese un numero: "))

    if (n == 1):
        primer_numero = numero
    elif (numero == primer_numero):
        cantidad_primer_numero = cantidad_primer_numero + 1
    
    if (numero > maximo):
        minimo = numero
        posicion_minimo = n

print("El mayor número ingresado es ", maximo," y lo ingresaste en la posición ",posicion_maximo)
print("El menor número ingresado es ", minimo," y lo ingresaste en la posición ",posicion_minimo)