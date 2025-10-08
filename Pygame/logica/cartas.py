import constantes
import random

def repartir_cartas():
# generamos la lista de cartas con 2 bucles for para palos y numeros
# generamos las cartas del mazo jugador y rival
# se utiliza .pop para evitar repetir cartas
    
    palos = constantes.PALOS
    numeros = constantes.NUMEROS       
    cartas = []

    for palo in palos:
        for numero in numeros:
            cartas.append((numero, palo))     


    random.shuffle(cartas)

    cartas_jugador = [cartas.pop() for _ in range(3)]

    cartas_rival = [cartas.pop() for _ in range(3)]

    return cartas_jugador, cartas_rival
