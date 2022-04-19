jugador1 = "Piedra"
jugador2 = "Papel"

def elegir_ganador(jugada1, jugada2, resultado):
    resultado = 0
    if (jugada1 != jugada2):
        if (jugada1 == "Piedra"):
            if (jugada2 == "Piedra"):
                resultado = 1
            else:
                resultado = 2
        elif (jugada1 == "Papel"):
            if (jugada2 == "Tijera"):
                resultado = 2
            else:
                resultado = 1
        else:
            if (jugada2 == "Piedra"):
                resultado = 2
            else:
                resultado = 1
        
    return resultado