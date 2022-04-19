def elevar(a, b):
    print(pow(a,b)) # La funcion pow eleva la potencia dada (pow(x,y) == x**y)
    """
    Recibe dos números como parámetro (base y exponente) y retorna el resultado de elevar base a la potencia exponente.
    """

numero1 = int(input("Ingrese el primer número que desea calcular: "))
numero2 = int(input("Ingrese el segundo número que desea calcular: "))
elevar(numero1,numero2)