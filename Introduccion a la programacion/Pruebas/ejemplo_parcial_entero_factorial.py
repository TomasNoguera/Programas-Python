def factorial(n):
    numero_fectorial = 1
    if n >= 0: #Como dice entero y no natural, es valido ya que no hay un factorial de n negativo.
        for _ in range(n):
            numero_fectorial = numero_fectorial * n
            n = n-1
        ret = numero_fectorial
    else:
        ret = "Math error"
    return ret