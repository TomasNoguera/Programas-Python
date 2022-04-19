nota = int(input('Ingrese una nota de parcial (1-10): '))
print('La nota ingresada es ' + str(nota))

if (nota > 10):
    print("Error! Solo puede ingresar una nota del 1 al 10")
if (nota < 1):
    print("Error! Solo puede ingresar una nota del 1 al 10")