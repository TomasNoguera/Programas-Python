def tipo_triangulo(lado1,lado2,lado3):
    
    if (lado1 == lado2 == lado3):
        return "Equilatero"
    if (lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3):
        return "Isosceles"
    if (lado1 != lado2) and (lado2 != lado3) and (lado1 != lado3):
        return "Escaleno"
    

print(tipo_triangulo(10,10,10))
print(tipo_triangulo(6,6,3))
print(tipo_triangulo(5,7,10))