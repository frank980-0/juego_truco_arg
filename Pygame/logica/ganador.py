from constantes import VALORES

def valor_truco(numero, palo):

    if (palo, numero) in VALORES:
        return VALORES[(palo, numero)]

    return VALORES[("", numero)]

def determinar_ganador(carta_jugador, carta_rival):
    vj = valor_truco(*carta_jugador)
    vr = valor_truco(*carta_rival)

    if vj > vr:
        return "jugador"
    elif vr > vj:
        return "rival"
    else:
        return "empate"
    
def ganador_partida(jugadas):
    puntos_jugador = 0
    puntos_rival = 0

    for carta_jugador, carta_rival in jugadas:
        ganador = determinar_ganador(carta_jugador, carta_rival)
        if ganador == "jugador":
            puntos_jugador += 1
        elif ganador == "rival":
            puntos_rival += 1

        # Primera a 2
        if puntos_jugador == 2:
            return "jugador"
        if puntos_rival == 2:
            return "rival"
    
    return "jugador"  # Por defecto, en caso de empate final