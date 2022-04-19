def factorial(numero): # Ejercio de un TP
    resultado = 1 # Devuelve el factorial del numero pasado por parametro Ej: 5! = 5*4*3*2*15
    for actual in range(1, numero + 1):
        resultado = resultado * actual
    return resultado

n = int(input("Inserte aqui: "))

ret = factorial(n)
print("Resultado: ", ret)
