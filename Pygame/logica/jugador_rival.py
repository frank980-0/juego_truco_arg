from . import cartas_mazo
import random

# repartimos las cartas para el jugador y rival

def repartir_cartas():
# generamos las cartas del mazo jugador y rival
# se utiliza .pop para evitar repetir cartas

    cartas = cartas_mazo.generar_cartas()
    random.shuffle(cartas)

    cartas_jugador = [cartas.pop() for _ in range(3)]

    cartas_rival = [cartas.pop() for _ in range(3)]

    return cartas_jugador, cartas_rival
