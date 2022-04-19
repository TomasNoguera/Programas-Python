def lado_valido(lado):

    return 20 >= lado >= 5

def tipo_triangulo():
    lado1 = None
    lado2 = None
    lado3 = None
    ret = ""
    
    try:
        lado1 = float(input("Ingrese el primer lado que desee calcular: "))
        lado2 = float(input("Ingrese el segundo lado que desee calcular: "))
        lado3 = float(input("Ingrese el tercer lado que desee calcular: "))
    except ValueError:
        ret = "Invalido"
    
    if ret == "":
        if lado_valido(lado1) and lado_valido(lado2) and lado_valido(lado3):
            if lado1 == lado2 == lado3:
                ret = "Equilatero"
            elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
                ret = "Isoceles"
            else:
                ret = "Escaleno"
        else:
            ret = "Invalido"   
    return ret

triangulo = tipo_triangulo()

print(triangulo)