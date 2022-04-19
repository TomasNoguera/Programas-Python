def entero_valido(numero):

        if (numero >= 0) and (numero <= 100):
            return True
        else:
            return False

print(entero_valido(98))